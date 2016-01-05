#!/usr/bin/env python

import requests, json

res_dict = {
    'package_id':'csvtest2',
    'name': '4918.test.t2.csv',
    'description': 'A file named 4918.test.t2.csv.',
    'url' : 'http://frc.robolog.org:5000'
}

res_url = 'http://frc-robolog.org:5000/api/action/resource_create'
auth = {'Authorization': 'APIKEY'}

f = [('upload', file('/home/frc/github/FRC-2016/Robolog/ApiTest/4918.test.t2.csv'))]
r = requests.post(res_url, data=res_dict, headers=auth, files=f)
