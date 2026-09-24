# MISSION: The complete set of examples and source code for ''Python 4000: Linux
# Commands & DevOps Automation''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-4000-Linux-DevOps
# DATE: 2019-06-29 15:30:00
# FILE: ex_argv_01.py
# AUTHOR: Randall Nagy
# Cerca: Slide 95
# Ref: https://docs.python.org/3/howto/argparse.html
# Actions: https://docs.python.org/3/library/argparse.html#action
#

import sys

print(type(sys.argv),len(sys.argv))
    
for cmd in sys.argv:
    print(cmd)

import argparse as Ape
#dir(Ape)
#help(Ape.ArgumentParser)
#help(Ape.ArgumentParser.add_argument)

parser = Ape.ArgumentParser()
parser.add_argument("-c", "--create",
                    action="store_true", # absence = 'store_false'
                    help="Create a record.")

args = parser.parse_args()
print(args)

'''
import os
os.popen("C:/study/ex_argv_01.py").read()
'''



    
