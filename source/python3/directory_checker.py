#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
import os
import sys
import time

import file_checker

DELAY = 1800  # check every 30 minutes


def check_directory(directory_path, last_check):
    if directory_path[-1] != "/":
        directory_path += "/"
    directory = os.listdir(directory_path)
    subdirectories = []
    for f in directory:
        path = f"{directory_path}{f}"
        if os.path.isfile(path):
            if last_check < datetime.fromtimestamp(os.path.getmtime(path)):
                print(path)
                file_checker.check_file(path)
        else:
            subdirectories.append(path)

    for sub_dir in subdirectories:
        check_directory(sub_dir, last_check)


def main(directory_path):
    last_check = datetime.min
    while True:
        check_directory(directory_path, last_check)
        last_check = datetime.now()
        time.sleep(DELAY)  # check directory every 30 min


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except Exception as e:
        print(e)
