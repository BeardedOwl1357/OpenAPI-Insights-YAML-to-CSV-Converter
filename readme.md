# OpenAPI Insights: YAML to CSV Converter

Table of Contents

- [OpenAPI Insights: YAML to CSV Converter](#openapi-insights-yaml-to-csv-converter)
- [What does this do?](#what-does-this-do)
- [Usecase](#usecase)
- [Usage](#usage)
  - [Install the following python packages](#install-the-following-python-packages)
  - [Provide the path of files](#provide-the-path-of-files)
  - [Execute the script](#execute-the-script)

# What does this do?

This converts an openapi yaml file to a csv file which contains some information at a high level in a CSV format. Each row contains the following:

- Tag of the endpoint : If the endpoint does not have a tag, the value `default` is used
- HTTP Method
- Summary of Endpoint
- Description of Endpoint
- Path
- Response Codes
- A field which indicates whether the endpoint has response codes for `success` operations (2xx) or not
- A field which indicates whether the endpoint has response codes for `failure` operations (4xx) or not
- A field which indicates whether the endpoint has response codes for `server failure` operations (5xx) or not

# Usecase

While creating openapi documentation, it was discovered that few endpoints did not have response codes for failure (4xx) and server failure (5xx). Instead of manually checking the documentation and noting the endpoints which do not have these responses, I decided to create a script which automates this process

# Usage

## Install the following python packages

- PyYAML : https://pyyaml.org/wiki/PyYAMLDocumentation
- csv : Package installed by default
- os : Package installed by default

## Provide the path of files

In the code, modify the following variables.

- For the yaml file : `INPUT_FNAME`
- For the output file : `OUTPUT_FNAME`

## Execute the script

| OS          | Terminal Command |
| ----------- | ---------------- |
| Windows     | python main.py   |
| Mac / Linux | python3 main.py  |
