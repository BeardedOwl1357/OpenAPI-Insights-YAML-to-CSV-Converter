import yaml
import csv
import os
# Open the file which contains data in YAML format
fname = os.path.join(os.getcwd(),"openapi.yaml")
file = open(fname)

# Open the file where we will write the data.
# If the file does not exist, a file will be created
# Name of the file will be the value of `ofname` variable
ofname = os.path.join(os.getcwd(),"output.csv")
ofile = open(ofname,"w")

# Load YAML content and convert it to python dictionary
data = yaml.safe_load(file)
print(data.keys())

# Prepare to write CSV data
# NOTE : Only the first tag is selected
fields = [
    "tag",
    "Method",
    "Endpoint",
    "summary",
    "description",
    "Responses",
    "HasSuccessResponse",
    "HasFailureResponse",
    "HasServerFailResponse"
    ]
csvWriter = csv.writer(ofile)
csvWriter.writerow(fields)

# Iterate over each path
for path in data["paths"]:
    # Iterate over each method in a path
    for method in data["paths"][path]:
        summary = data["paths"][path][method]["summary"]
        description = data["paths"][path][method]["description"]
        tag = data["paths"][path][method]["tags"][0]
        # Get list of responses
        responses = list(data["paths"][path][method]["responses"].keys())
        hasSuccess, hasFailure , hasServerFailure = False,False,False
        # Iterate over each response and check the first "digit"
        # Each response is stored as a string, not a number so we can do this
        for response in responses:
            if(response[0] == '2'):
                hasSuccess = True
            elif(response[0] == '4'):
                hasFailure = True
            elif(response[0] == '5'):
                hasServerFailure = True
        # Prepare and write the CSV row
        # Responses are separated by \t (tab). Don't use commas.
        output = [
            tag,
            method,
            path,
            summary,
            description,
            " \t ".join(responses),
            hasSuccess,
            hasFailure,
            hasServerFailure
            ]
        csvWriter.writerow(output)

# Close the files which we had opened earlier
file.close()
ofile.close()