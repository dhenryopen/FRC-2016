#!/usr/bin/env python
#
# create_robolog_resource.py -- create a CKAN resource (i.e. individual file) for a metrics log file (1:1 relationship)
#
#   This program is called by create_robolog_resource.sh and should be run once per event (i.e. practice or FRC competition)
#

import argparse
import json
import requests
import pprint
import robolog

# Define the command-line arguments

parser = argparse.ArgumentParser(prog='create_robolog_resource',
                                 description='A program to upload a Robolog metrics log',
                                 formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50,
                                                                                     width=130))

parser.add_argument('--config_file', action='store', dest='config_file', required=True,
                    help='The name and path to the Robolog config file')
parser.add_argument('--metrics_file', action='store', dest='metrics_file', required=True,
                    help='The name and path to the metrics file to upload')
parser.add_argument('--description', action='store', dest='description', default='None',
                    help='An optional description')
parser.add_argument('--debug', '-d', action='store_true', help='Print the result of the CKAN "resource_create" API call')

parameters = parser.parse_args()

# Parse the configuration file values

robolog.Config.read(parameters.config_file)

# Assign configuration values to dictionary variables

ckan_apikey = robolog.ConfigSectionMap("robolog:ckan")['ckan_apikey']
ckan_package_id = robolog.ConfigSectionMap("robolog:ckan")['ckan_name']
server = robolog.ConfigSectionMap("robolog:frc")['server']

# Create two dictionaries that we can pass to the CKAN REST API

resource_dict = {
    'package_id': ckan_package_id,  # corresponds with the dataset name in the containing package
    'name': parameters.metrics_file,
    'description': parameters.description,
    'url': ''
}

# Make the REST call

request_url = server + '/api/action/resource_create'

headers = {
    'Authorization': ckan_apikey
}

# Encode the metrics log file name

file = [('upload', file(parameters.metrics_file))]

print 'Attempting to upload "' + parameters.metrics_file + '" to ' + server + ' using the config file "' + parameters.config_file + '"'

response = requests.post(request_url, data=resource_dict, headers=headers, files=file)

# Optionally print the result

if parameters.debug:
    pprint.pprint(json.loads(response.content))

print 'Done'
