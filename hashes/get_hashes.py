#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

SITE = "https://virusshare.com/hashfiles/"
FILE = "VirusShare_"
EXTENSION = ".md5"
NUM_FILES = 390

for current in range(0, NUM_FILES):
    url = f"{SITE}{FILE}{'0' * (5 - len(str(current))) + str(current)}{EXTENSION}"
    r = requests.get(url)
    lines = r.text.split("\n")
    for i in range(6, len(lines)):
        print(lines[i])
