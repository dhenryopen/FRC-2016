
import requests, json

res_dict = {
    'package_id':'test5',
    'name': 'Yet another dataset',
    'description': 'Dataset created through Python',

#    'url' : 'http://frc.robolog.org:5000'
}

res_url = 'http://frc-robolog.org:5000/api/action/package_create'
auth = {'Authorization': 'c1fe0417-a8d9-49b4-a4e2-4fe18e9438d1'}
#f = [('upload', file('/home/frc/PycharmProjects/ckanapi/4918.test.t2.json'))]

#r = requests.post(res_url, data=res_dict, headers=auth, files=f)
r = requests.post(res_url, data=res_dict, headers=auth)
