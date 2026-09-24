# MISSION: The complete set of examples and source code for ''Python 4000: Linux
# Commands & DevOps Automation''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-4000-Linux-DevOps
# DATE: 2019-07-02 15:30:00
# FILE: ex_107_ape_remainders.py
# AUTHOR: Randall Nagy
#
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("message",
                    nargs=argparse.REMAINDER)
parser.add_argument("-c", "--create",
                    action="store_true",
                    help="Log message")
print(parser.parse_args(
    '-c This is a test'.split())
      )
