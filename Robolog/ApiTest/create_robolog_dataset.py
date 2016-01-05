#!/usr/bin/env python
#
# create_robolog_dataset.py -- create a CKAN dataset (i.e. package) to contain a set of metrics log files
#
#   This program is called by create_robolog_dataset.sh and should be run once per match (i.e. once per log file)
#   Log file names MUST be unique within the scope of a CKAN dataset
#

import urllib2
import urllib
import json
import ConfigParser
import requests
import pprint

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


Config.read('robolog.cfg')

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

# Use the json module to dump the dictionary to a string for posting

data_string = urllib.quote(json.dumps(dataset_dict))

# Use the "package_create" function to create a new dataset

request = urllib2.Request(server + '/api/action/package_create')

# Create an authorization header with the CKAN API

request.add_header('Authorization', ckan_apikey)

# Make the REST request

response = urllib2.urlopen(request, data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary

response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result
# print the contents for debugging purposes

created_package = response_dict['result']
pprint.pprint(created_package)
