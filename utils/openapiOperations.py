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
        firstDigit = response[0]
        if(int(firstDigit) < 1 or int(firstDigit) > 6):
            continue
        key = f"{firstDigit}xx"
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