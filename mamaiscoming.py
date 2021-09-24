#!/usr/bin/python
# -*-coding : utf-8 -*
import os
import subprocess

#list_path = os.system("find /home -iname \"porn\"*")
list_path = subprocess.check_output("find /home -iname \"porn*\"", shell=True).decode("utf-8").split("\n")
list_path.pop(len(list_path) - 1)
#print(list_path)
for item in list_path:
    os.system("rm -fv " + item)
