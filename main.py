#!/usr/local/bin/python3
import os
import csv
from constants import fileConstants
from constants import openapiConstants
from utils import openapiOperations
from utils import fileOperations

def getAbsolutePath(path):
    return os.path.join(os.getcwd(),path)

# Read and convert YAML data to Python Dictionary
data = fileOperations.read_yaml(getAbsolutePath(fileConstants.INPUT_FNAME))
# Open a CSV File
oFile = open(getAbsolutePath(fileConstants.OUTPUT_FNAME),"w")
csvWriter = csv.writer(oFile)
# Write Header Row
fileOperations.write_to_csv(csvWriter,fileConstants.CSV_FIELDS)

# Iterate over each path
for path in data["paths"]:
    # Iterate over each method in a path
    for method in data["paths"][path]:
        pathItem = data["paths"][path][method]        
        # Get list of responses
        responses = openapiOperations.getResponses(pathItem=pathItem)
        responseTypes = openapiOperations.getTypesOfResponses(responses)
        # Prepare and write the CSV row
        # Responses are separated by \t (tab). Don't use commas.
        output = [
            # Only first tag is used
            pathItem.get("tags",[openapiConstants.DEFAULT_TAG])[0],
            method,
            path,
            pathItem.get("summary",""),
            pathItem.get("description",""),
            " \t ".join(responses),
            responseTypes['2xx'],
            responseTypes['4xx'],
            responseTypes['5xx']
            ]
        fileOperations.write_to_csv(csvWriter,output)
        # Creating Report
        openapiOperations.updateTagInfo(pathItem.get("tags",[openapiConstants.DEFAULT_TAG])[0])

# Close the files which we had opened earlier
oFile.close()

openapiOperations.printReport()
