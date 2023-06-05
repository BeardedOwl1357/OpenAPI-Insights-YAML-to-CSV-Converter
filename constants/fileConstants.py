import os
# Input File
fname = os.path.join(os.getcwd(),"openapi.yaml")

# Output File
ofname = os.path.join(os.getcwd(),"main.csv")

# CSV File Fields
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
