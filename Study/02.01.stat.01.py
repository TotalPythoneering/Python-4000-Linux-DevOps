#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 4000: Linux
# Commands & DevOps Automation''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-4000-Linux-DevOps
# DATE: 2019-04-09 15:30:00
# FILE: 02.01.stat.01.py
# AUTHOR: Randall Nagy
#

from os import popen

zfile = "./foo.txt"
"""
with open(zfile, "w") as fh:
    fh.write("Hello, file")

with open(zfile) as fh:
    print(*fh)
"""
print(*popen("stat " + zfile))

print(*popen("touch " + zfile))

print(*popen("stat " + zfile))

print(*popen("chmod -x " + zfile))

print(*popen("stat " + zfile))


    
