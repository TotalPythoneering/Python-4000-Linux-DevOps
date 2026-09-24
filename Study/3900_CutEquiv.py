# MISSION: The complete set of examples and source code for ''Python 4000: Linux
# Commands & DevOps Automation''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-4000-Linux-DevOps
# DATE: 2019-04-17 15:30:00
# FILE: 3900_CutEquiv.py
# AUTHOR: Randall Nagy
# cal -3 > three.txt
# cut -c 15-17,37-39,59-61 three.txt
#

root = 'c:/MyCygwin/home/Randall/three.txt'
cmd = ["cal", "-3", ">", root]
from subprocess import Popen
print('Code:', Popen(cmd, shell=True).wait())
with open(root) as fh:
    for line in fh:
        print(line[14:17], line[36:39], line[58:61])
            
        
