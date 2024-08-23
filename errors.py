#!/usr/bin/env python3
import os
import sys

# LBYL - Look Before You Leap

if os.path.exists("names.txt"):
    print("The file exist")
    print("...")            # Race condition
    names = open("names.txt").readlines()
else:
    print("[Error] - Fille names.txt not found")
    sys.exit(1)


if len(names) >= 3:
    print(names[2])
else:
    print("[Error] - Missing name in the list")
    sys.exit(1)