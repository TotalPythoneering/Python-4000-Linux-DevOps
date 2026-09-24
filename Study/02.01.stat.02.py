#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 4000: Linux
# Commands & DevOps Automation''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-4000-Linux-DevOps
# DATE: 2019-04-09 15:30:00
# FILE: 02.01.stat.02.py
# AUTHOR: Randall Nagy
#

from os import stat

zfile = "./foo.txt"

print("\n"*50)

with open(zfile, "w") as fh:
    fh.write("Hello, file")

with open(zfile) as fh:
    print(*fh)

print(*stat(zfile))


    
