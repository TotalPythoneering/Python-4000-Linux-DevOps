# MISSION: The complete set of examples and source code for ''Python 4000: Linux
# Commands & DevOps Automation''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-4000-Linux-DevOps
# DATE: 2019-06-29 15:30:00
# FILE: foo.py
# AUTHOR: Randall Nagy
# File:  ape01.py
# Cerca: Python 4000 - Linux DevOps: Slide 95
#

import argparse as Ape
parser = Ape.ArgumentParser()
parser.add_argument("-c", "--create",
                    action="store_true",
                    help="Create a record.")

args = parser.parse_args()
print("Running with:", args)

''' Driver:
import os;print(os.popen("C:/study/ape01.py -h").read())
'''



    
