#!/usr/bin/env python
#
# create_robolog_dataset.py -- create a CKAN dataset (i.e. package) to contain a set of metrics log files
#
#   This program is called by create_robolog_dataset.sh and should be run once per match (i.e. once per log file)
#   Log file names MUST be unique within the scope of a CKAN dataset
#

import argparse
import json
import ConfigParser
import requests
import pprint

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

Config = ConfigParser.RawConfigParser()


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


Config.read(parameters.config_file)

# Assign configuration values to dictionary variables

ckan_apikey = ConfigSectionMap("robolog:ckan")['ckan_apikey']
ckan_author = ConfigSectionMap("robolog:ckan")['ckan_author']
ckan_author_email = ConfigSectionMap("robolog:ckan")['ckan_author_email']
ckan_maintainer = ConfigSectionMap("robolog:ckan")['ckan_maintainer']
ckan_maintainer_email = ConfigSectionMap("robolog:ckan")['ckan_maintainer_email']
ckan_name = ConfigSectionMap("robolog:ckan")['ckan_name']
ckan_notes = ConfigSectionMap("robolog:ckan")['ckan_notes']
ckan_owner_org = ConfigSectionMap("robolog:ckan")['ckan_owner_org']
ckan_title = ConfigSectionMap("robolog:ckan")['ckan_title']
ckan_version = ConfigSectionMap("robolog:ckan")['ckan_version']

cfg_file = ConfigSectionMap("robolog:frc")['cfg_file']
district = ConfigSectionMap("robolog:frc")['district']
driver = ConfigSectionMap("robolog:frc")['driver']
event = ConfigSectionMap("robolog:frc")['event']
eventlat = ConfigSectionMap("robolog:frc")['eventlat']
eventlon = ConfigSectionMap("robolog:frc")['eventlon']
match = ConfigSectionMap("robolog:frc")['match']
robot = ConfigSectionMap("robolog:frc")['robot']
server = ConfigSectionMap("robolog:frc")['server']
station = ConfigSectionMap("robolog:frc")['station']
teamname = ConfigSectionMap("robolog:frc")['teamname']
teamnumber = ConfigSectionMap("robolog:frc")['teamnumber']

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
