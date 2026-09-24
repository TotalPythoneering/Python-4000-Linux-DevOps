#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 4000: Linux
# Commands & DevOps Automation''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-4000-Linux-DevOps
# DATE: 2019-06-29 15:30:00
# FILE: param_test.py
# AUTHOR: Randall Nagy
#

import sys

for ss, word in enumerate(sys.argv, 1):
    print(ss, word)

print("Done!")

