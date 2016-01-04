#!/usr/bin/env python

import requests, json

res_dict = {
    'package_id':'csvtest',
    # 'name': '4918.test.t1.csv',
    'name': '4918.test.t1.json',
    # 'description': 'A file named 4918.test.t1.csv.',
    'description': 'A file named 4918.test.t1.json.',
    'url' : 'http://frc.robolog.org:5000'
}

res_url = 'http://frc-robolog.org:5000/api/action/resource_create'
auth = {'Authorization': 'c1fe0417-a8d9-49b4-a4e2-4fe18e9438d1'}
# f = [('upload', file('/home/frc/github/FRC-2016/Robolog/ApiTest/4918.test.t1.csv'))]
f = [('upload', file('/home/frc/github/FRC-2016/Robolog/ApiTest/4918.test.t1.json'))]

r = requests.post(res_url, data=res_dict, headers=auth, files=f)

