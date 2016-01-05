#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import ConfigParser

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

Config.read('robolog.cfg')  # read the site-specific settings and assign to dictionary variables

ckan_apikey = ConfigSectionMap("robolog:ckan")['ckan_apikey']
ckan_author = ConfigSectionMap("robolog:ckan")['ckan_author']
ckan_author_email = ConfigSectionMap("robolog:ckan")['ckan_author_email']
ckan_maintainer = ConfigSectionMap("robolog:ckan")['ckan_maintainer']
ckan_maintainer_email = ConfigSectionMap("robolog:ckan")['ckan_maintainer_email']
ckan_name = ConfigSectionMap("robolog:ckan")['ckan_name']
ckan_notes = ConfigSectionMap("robolog:ckan")['ckan_notes']
ckan_owner_org = ConfigSectionMap("robolog:ckan")['ckan_owner_org']
ckan_url = ConfigSectionMap("robolog:ckan")['ckan_url']
ckan_version = ConfigSectionMap("robolog:ckan")['ckan_version']

cfg_file = ConfigSectionMap("robolog:frc")['cfg_file']
district = ConfigSectionMap("robolog:frc")['district']
event = ConfigSectionMap("robolog:frc")['event']
eventlat = ConfigSectionMap("robolog:frc")['eventlat']
eventlon = ConfigSectionMap("robolog:frc")['eventlon']
match = ConfigSectionMap("robolog:frc")['match']
robot = ConfigSectionMap("robolog:frc")['robot']
server = ConfigSectionMap("robolog:frc")['server']
teamname = ConfigSectionMap("robolog:frc")['teamname']
teamnumber = ConfigSectionMap("robolog:frc")['teamnumber']

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'title': ckan_name,
    'name': ckan_name,
    'author': ckan_author,
    'author_email': ckan_author_email,
    'maintainer': ckan_maintainer,
    'maintainer_email': ckan_maintainer_email,
    'notes': ckan_notes,
    'owner_org': ckan_owner_org,
    'url': ckan_url,
    'version': ckan_version,
    'tags': [{'name': district},
             {'name': event},
             {'name': eventlat},
             {'name': eventlon},
             {'name': match},
             {'name': robot},
             {'name': teamname},
             {'name': teamnumber}]
}

# Use the json module to dump the dictionary to a string for posting.
data_string = urllib.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib2.Request(server + '/api/action/package_create')
#request = urllib2.Request('http://frc-robolog.org:5000/api/action/package_update')

# Creating a dataset requires an authorization header.

# frc-robolog.org
request.add_header('Authorization', ckan_apikey)

# Make the HTTP request.
response = urllib2.urlopen(request, data_string) #, tag_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)




