import constants.fileConstants as fileConstants
import yaml
import os
import csv

def read_yaml(yaml_file:str):
    # Open the file which contains data in YAML format
    file = open(yaml_file)
    data = file.read()
    file.close()
    return yaml.safe_load(clean_yaml_file(data))

def clean_yaml_file(yaml_file:str):
    ''' 
        Refer to this link : https://stackoverflow.com/questions/55902201/python-yaml-yaml-reader-readererror-unacceptable-character
    '''
    file_cleaning_characters = {
        '\u0000':''
    }
    for character,replacingCharacter in file_cleaning_characters.items():
        print("{:20s}{:20s}".format(character,replacingCharacter))
        yaml_file = yaml_file.replace(character,replacingCharacter)
    return yaml_file

def clean_csv_file(csv_file:str):
    pass

def write_to_csv(
        csvWriter,
        row:list
        ):
    if(len(row) != fileConstants.NUM_CSV_FIELDS):
        # DEBUG Message
        print(f"{'*' * 15} ERROR : Number of fields in row not equal to required {'*' * 15}")
    csvWriter.writerow(row)