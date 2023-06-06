import os
# Input File
INPUT_FNAME = os.path.join(os.getcwd(),"openapi.yaml")

# Output File
OUTPUT_FNAME = os.path.join(os.getcwd(),"output.csv")

# CSV File CSV_FIELDS
# NOTE : Only the first tag is selected
CSV_FIELDS = [
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
NUM_CSV_FIELDS = len(CSV_FIELDS)