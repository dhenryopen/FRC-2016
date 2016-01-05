#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'title': 'CSV Test',    # default is same as "name"
    'name': 'csvtest',
    # 'author': '',
    # 'author_email': '',
    # 'maintainer': '',
    # 'maintainer_email': '',
    # 'license_id': '',
    'notes': 'Comma-delimited with header row',
    # 'url': '',
    'version': '0.9',
    # 'state': '',   # default is 'active'
    # 'type': '',
    # 'resources': '',
    'tags': [{'name': 'District.PNW'},
             {'name': 'Team.4918'},
             {'name': 'Event.CMP'},
             {'name': 'Match.Q2'},
             {'name': 'Robot.BUGSY'}],
    # 'extras': '',
    # 'relationships_as_object': '',
    # 'relationships_as_subject': '',
    # 'group': '',
    'owner_org': 'team-4918'
}

# Use the json module to dump the dictionary to a string for posting.
data_string = urllib.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib2.Request('http://frc-robolog.org:5000/api/action/package_create')
#request = urllib2.Request('http://frc-robolog.org:5000/api/action/package_update')

# Creating a dataset requires an authorization header.

# frc-robolog.org
request.add_header('Authorization', 'c1fe0417-a8d9-49b4-a4e2-4fe18e9438d1')

# Make the HTTP request.
response = urllib2.urlopen(request, data_string) #, tag_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)


# author = Dave Henry
# author_email = dshenry99@gmail.com
# district = District.PNW
# event = Event.PRACT
# eventlat = EventLat.48.101
# eventlon = EventLon.-122.799
# maintainer = Dave Henry
# maintainer_email = dshenry99@gmail.com
# match = Match.P1
# notes = Log generated during team practice
# owner_org = team-4918
# robot = Robot.BUSTER
# teamname = TeamName.Roboctopi
# teamnumber = TeamNumber.4918
# version = 0.9
