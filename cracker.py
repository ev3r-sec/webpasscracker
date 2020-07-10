#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author: ev3r

import requests
url = 'www.test.org'
data = {'username': 'user', 'password': '123456'}
session = requests.Session()
session.get(url)
response = session.post(url, data,)
