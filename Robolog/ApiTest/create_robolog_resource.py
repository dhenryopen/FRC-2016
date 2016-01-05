#!/usr/bin/env python
#
# create_robolog_resource.py -- create a CKAN resource (i.e. individual file) for a metrics log file (1:1 relationship)
#
#   This program is called by create_robolog_resource.sh and should be run once per event (i.e. practice or FRC competition)
#

import argparse
import json
import ConfigParser
import requests

# Define the command-line arguments

parser = argparse.ArgumentParser(prog='create_robolog_resource',
                                 description='A program to upload a rooblog metrics log',
                                 formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50,
                                                                                     width=130))

parser.add_argument('--config_file', action='store', dest='config_file', required=True,
                    help='The name and path to the robologs config file')

parser.add_argument('--metrics_file', action='store', dest='metrics_file', required=True,
                    help='The name and path to the metrics file to upload')

parser.add_argument('--description', action='store', dest='description', default='None',
                    help='An optional description')

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

# Map command-line arguments to configuration file values

ckan_apikey = ConfigSectionMap("robolog:ckan")['ckan_apikey']
ckan_package_id = ConfigSectionMap("robolog:ckan")['ckan_name']
server = ConfigSectionMap("robolog:frc")['server']

# Create two dictionaries that we can pass to the CKAN REST API

res_dict = {
    'package_id': ckan_package_id,  # corresponds with the dataset name in the containing package
    'name': parameters.metrics_file,
    'description': parameters.description,
    'url': ''
}

res_url = server + '/api/action/resource_create'
auth = {
    'Authorization': ckan_apikey
}

# Make the REST request

f = [('upload', file(parameters.metrics_file))]
print 'Attempting to send ' + parameters.metrics_file + ' to ' + server + ' using the config file "' + parameters.config_file + '"'
r = requests.post(res_url, data=res_dict, headers=auth, files=f)
print 'Done'
