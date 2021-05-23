#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import database as db

SITE = "https://virusshare.com/hashfiles/"
FILE = "VirusShare_"
EXTENSION = ".md5"
NUM_FILES = 390
# NUM_THREADS = 8


# For multithreading
def get_hashes(start, end):
    for current in range(start, end):
        url = f"""{SITE}{FILE}{'0' * (5 - len(str(current))) +
                                                    str(current)}{EXTENSION}"""
        print(url)
        r = requests.get(url)
        lines = r.text.split("\n")[6:-1]
        db.insert_hash(str(lines).replace("[", "").replace("]", ""), num=len(lines))


db.create_db()
get_hashes(0, NUM_FILES)
