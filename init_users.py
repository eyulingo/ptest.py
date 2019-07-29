#!/usr/bin/env python

import json
import names
import random
import requests

secret_key = "BE?kmix8kj$j(V^$]8p("

register_uri = "http://47.103.15.32:8080/register"
s = requests.session()

count_limit = 1000

csv_string = ""

headers = {'Content-Type': 'application/json'}

counter = 0
while counter < count_limit:
    username = names.get_first_name(gender='female') + str(random.randint(100, 999))

    if len(username) < 7:
        continue
    password = username.replace(' ', '') + str(random.randint(1000, 9999))

    email = str(random.randint(800000, 10000000)) + "@qq.com"
    
    params = {
        'email': email,
        'username': username,
        'password': password,
        'confirm_password': password,
        'confirm_code': secret_key
    }
    r = s.post(register_uri, headers=headers, data=json.dumps(params))

    if r.json()['status'] == 'ok':
        print("  Successfully created user #%d: %s" % (counter, username))
        csv_string += (username + "," + password + "\n")
    else:
        print("! Failed to created user #%s. Error Code: %s" % (username, r.json()['status']))
        print("\tDetailed Status: %s" % r.content.decode())
    counter += 1

with open('generated.users.csv', 'w') as f:
    f.write(csv_string)