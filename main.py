#!/usr/local/bin/python3
import yaml
import csv
import os
from constants import fileConstants
from utils import openapiOperations

# Open the file which contains data in YAML format
file = open(fileConstants.fname)

# Open the file where we will write the data.
# If the file does not exist, a file will be created
# Name of the file will be the value of `ofname` variable
ofile = open(fileConstants.ofname,"w")

# Load YAML content and convert it to python dictionary
data = yaml.safe_load(file)
# print(data.keys())

# Prepare to write CSV data
csvWriter = csv.writer(ofile)
csvWriter.writerow(fileConstants.fields)


# Iterate over each path
for path in data["paths"]:
    # Iterate over each method in a path
    for method in data["paths"][path]:
        pathItem = data["paths"][path][method]        
        # Get list of responses
        responses = list(pathItem["responses"].keys())
        responseTypes = openapiOperations.getTypesOfResponses(responses)
        # Prepare and write the CSV row
        # Responses are separated by \t (tab). Don't use commas.
        output = [
            # Only first tag is used
            pathItem["tags"][0],
            method,
            path,
            pathItem["summary"],
            pathItem["description"],
            " \t ".join(responses),
            responseTypes['2xx'],
            responseTypes['4xx'],
            responseTypes['5xx']
            ]
        csvWriter.writerow(output)
        # Creating Report
        openapiOperations.updateTagInfo(pathItem["tags"][0])

# Close the files which we had opened earlier
file.close()
ofile.close()

openapiOperations.printReport()
