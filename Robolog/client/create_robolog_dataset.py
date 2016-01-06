#!/usr/bin/env python
#
# create_robolog_dataset.py -- create a CKAN dataset (i.e. package) to contain a set of metrics log files
#
#   This program is called by create_robolog_dataset.sh and should be run once per match (i.e. once per log file)
#   Log file names MUST be unique within the scope of a CKAN dataset
#

import argparse
import json
import requests
import pprint
import robolog

# Define the command-line arguments

parser = argparse.ArgumentParser(prog='create_robolog_dataset',
                                 description='A program to create a container for Robolog files',
                                 formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50,
                                                                                     width=130))

parser.add_argument('--config_file', action='store', dest='config_file', required=True,
                    help='The name and path to the Robolog config file')
parser.add_argument('--debug', '-d', action='store_true',
                    help='Print the result of the CKAN "package_create" API call')

parameters = parser.parse_args()

# Parse the configuration file values

robolog.Config.read(parameters.config_file)

# Assign configuration values to dictionary variables

# Specific to CKAN

ckan_apikey = robolog.ConfigSectionMap("robolog:ckan")['ckan_apikey']
ckan_author = robolog.ConfigSectionMap("robolog:ckan")['ckan_author']
ckan_author_email = robolog.ConfigSectionMap("robolog:ckan")['ckan_author_email']
ckan_maintainer = robolog.ConfigSectionMap("robolog:ckan")['ckan_maintainer']
ckan_maintainer_email = robolog.ConfigSectionMap("robolog:ckan")['ckan_maintainer_email']
ckan_name = robolog.ConfigSectionMap("robolog:ckan")['ckan_name']
ckan_notes = robolog.ConfigSectionMap("robolog:ckan")['ckan_notes']
ckan_owner_org = robolog.ConfigSectionMap("robolog:ckan")['ckan_owner_org']
ckan_title = robolog.ConfigSectionMap("robolog:ckan")['ckan_title']
ckan_version = robolog.ConfigSectionMap("robolog:ckan")['ckan_version']

# Specific to Robolog

cfg_file = robolog.ConfigSectionMap("robolog:frc")['cfg_file']
district = robolog.ConfigSectionMap("robolog:frc")['district']
driver = robolog.ConfigSectionMap("robolog:frc")['driver']
event = robolog.ConfigSectionMap("robolog:frc")['event']
eventlat = robolog.ConfigSectionMap("robolog:frc")['eventlat']
eventlon = robolog.ConfigSectionMap("robolog:frc")['eventlon']
match = robolog.ConfigSectionMap("robolog:frc")['match']
robot = robolog.ConfigSectionMap("robolog:frc")['robot']
server = robolog.ConfigSectionMap("robolog:frc")['server']
station = robolog.ConfigSectionMap("robolog:frc")['station']
teamname = robolog.ConfigSectionMap("robolog:frc")['teamname']
teamnumber = robolog.ConfigSectionMap("robolog:frc")['teamnumber']

# Create a dictionary that we can pass to the CKAN REST API

dataset_dict = {
    'author': ckan_author,
    'author_email': ckan_author_email,
    'maintainer': ckan_maintainer,
    'maintainer_email': ckan_maintainer_email,
    'name': ckan_name.lower(),  # must be lower case and unique
    'notes': ckan_notes,
    'owner_org': ckan_owner_org,
    'title': ckan_title,
    'url': ckan_name.lower(),  # must be unique so set it to 'name' (which also must be unique)
    'version': ckan_version,
    'tags': [{'name': district},
             {'name': driver},
             {'name': event},
             {'name': eventlat},
             {'name': eventlon},
             {'name': match},
             {'name': robot},
             {'name': station},
             {'name': teamname},
             {'name': teamnumber}]
}

# Make the REST call

request_url = server + '/api/action/package_create'

headers = {
    'Authorization': ckan_apikey,
    'Content-type': 'application/json'
}

print 'Attempting to create dataset "' + dataset_dict[
    'name'] + '" on ' + server + ' using the config file "' + parameters.config_file + '"'

response = requests.post(request_url, data=json.dumps(dataset_dict), headers=headers)

# Optionally print the result

if parameters.debug:
    pprint.pprint(json.loads(response.content))

print 'Done'
