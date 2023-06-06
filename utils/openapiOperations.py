def isValidHttpResponse(response:str):
    '''
    A valid response is an HTTP response code of any form below
        - 1xx
        - 2xx
        - 3xx
        - 4xx
        - 5xx
    '''
    validResponses = ['1','2','3','4','5']
    isValid = False
    for resp in validResponses:
        if response[0] == resp:
            isValid = True
    return isValid

def getResponses(pathItem):
    responses = []
    for response in pathItem["responses"]:
        if isValidHttpResponse(response):
            responses.append(response)
    return responses

def getTypesOfResponses(responses):
    # Iterate over each response and check the first "digit"
    # Each response is stored as a string, not a number so we can do this
    responseTypes = {
        "1xx" : False,
        "2xx" : False,
        "3xx" : False,
        "4xx" : False,
        "5xx" : False
    }
    for response in responses:
        if(isValidHttpResponse(response)):
            key = f"{response[0]}xx"
            responseTypes[key] = True
    return responseTypes

tags = {}

def updateTagInfo(tag):
    tags[tag] = tags.get(tag,0) + 1

def printRow(
        *vals,
        paddingLength = 30,
        paddingCharacter = " ",
        startString = "",
        endString = ""):
    for val in vals:
        val = str(val).ljust(paddingLength,paddingCharacter[0])
        startString += f'{val}{endString}'
    print(startString)

def printMarkdownRow(
        *vals,
        paddingLength = 30,
        paddingCharacter = " ",
        startString = "|",
        endString = "|"):
    for val in vals:
        val = str(val).ljust(paddingLength,paddingCharacter[0])
        startString += f'{val}{endString}'
    print(startString)

def printMarkdownHeader(
        *headers,
        paddingLength = 30
        ):
    startString = "|"
    sep = "|"
    for header in headers:
        header = str(header).ljust(paddingLength)
        startString += f'{header}|'

        sep += "".ljust(paddingLength,"-")+"|"
    print(startString)
    print(sep)


def printReport():
    printRow(""," Report ","",paddingCharacter="-")
    
    print("# Endpoints per tag\n")
    printMarkdownHeader("Tag","Number of Endpoints")
    total_endpoints = 0
    for tag,num in tags.items():
        total_endpoints += num
        printMarkdownRow(tag,num)
    print()
    print("Total Endpoints = ",total_endpoints)