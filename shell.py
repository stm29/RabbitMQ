#!/usr/bin/env python
import subprocess, os

#using OS.system to sun bash command
os.system("echo Hello from the other side!")

home_dir = os.system("cd /")
print("`cd ~` ran with exit code %d" % home_dir)
unknown_dir = os.system("cd doesnotexist")
print("`cd doesnotexis` ran with exit code %d" % unknown_dir)

#Listing a particular directory in linux
dir_list = os.listdir('/')
print(dir_list)

#using subprocess for running bash command
list_files = subprocess.check_call(["ls", "-l"])
print("The exit code was: %d" % list_files)
