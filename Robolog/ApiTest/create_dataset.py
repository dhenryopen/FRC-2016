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

apikey = ConfigSectionMap("robolog")['apikey']
author = ConfigSectionMap("robolog")['author']
author_email = ConfigSectionMap("robolog")['author_email']
district = ConfigSectionMap("robolog")['district']
event = ConfigSectionMap("robolog")['event']
eventlat = ConfigSectionMap("robolog")['eventlat']
eventlon = ConfigSectionMap("robolog")['eventlon']
maintainer = ConfigSectionMap("robolog")['maintainer']
maintainer_email = ConfigSectionMap("robolog")['maintainer_email']
match = ConfigSectionMap("robolog")['match']
name = ConfigSectionMap("robolog")['name']
notes = ConfigSectionMap("robolog")['notes']
owner_org = ConfigSectionMap("robolog")['owner_org']
robot = ConfigSectionMap("robolog")['robot']
teamname = ConfigSectionMap("robolog")['teamname']
teamnumber = ConfigSectionMap("robolog")['teamnumber']
url = ConfigSectionMap("robolog")['url']
version = ConfigSectionMap("robolog")['version']

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'title': name,
    'name': name,
    'author': author,
    'author_email': author_email,
    'maintainer': maintainer,
    'maintainer_email': maintainer_email,
    'notes': notes,
    'owner_org': 'team-4918',
    'url': url,
    'version': version,
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
request = urllib2.Request('http://frc-robolog.org:5000/api/action/package_create')
#request = urllib2.Request('http://frc-robolog.org:5000/api/action/package_update')

# Creating a dataset requires an authorization header.

# frc-robolog.org
request.add_header('Authorization', apikey)

# Make the HTTP request.
response = urllib2.urlopen(request, data_string) #, tag_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)




