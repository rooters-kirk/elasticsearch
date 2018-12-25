#!/usr/bin/python
#-*- coding: utf-8 -*-

import json

json_file = {
    "name": "Hong",
    "birth": "0525",
    "age": 30
}

json_dumps_file = json.dumps(json_file) + "\n"

i = 0

while i < 30:
    with open('empty.json', 'a') as f:
        f.write(json_dumps_file)
    i += 1
