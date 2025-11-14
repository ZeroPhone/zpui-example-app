#!/usr/bin/env python3

"""
This script checks your repository for forgotten README items and files that you should change or remove before release.
It returns 0 if everything's fine and 1 if it looks like you forgot something.
"""

import os
import sys

red = "\x1b[31;20m"
yellow = "\x1b[33;20m"
reset = "\x1b[0m"

i = 1

def print_error(line, extra=""):
    global i
    if extra:
        print(str(i)+": "+red+line+reset+" ("+extra+")")
    else:
        print(str(i)+": "+red+line+reset)
    i += 1

def print_suggestion(line, extra=""):
    if extra:
        print("suggestion: "+yellow+line+reset+" ("+extra+")")
    else:
        print("suggestion: "+yellow+line+reset)

if os.path.exists("rename.py"):
    print_suggestion("rename.py file left in the repo", "is worth deleting to avoid confusion")

try:
    with open("README.md", "r") as f:
        readme_contents = f.read()
except:
    print_error("README.md gone? That's not workable =(")
    import traceback; traceback.print_exc()

lines = readme_contents.split("\n")
for j, line in enumerate(lines):
    if "gitlab.com" in line:
        print_suggestion("GitLab mention found on line {}, remember to change it you're using GitHub".format(j), repr(line))
    if "(**dev-only**)" in line:
        print_error("'dev-only' marked (line {}) left over in README".format(j), repr(line))
    if "This is an example app" in line:
        print_error("Example app stub text (line {}) left over in README".format(j), repr(line))
    if "NEWAPPNAME" in line:
        print_error("NEWAPPNAME left in line {}".format(j), repr(line))
    if "AUTHOR" in line:
        print_error("AUTHOR left in line {}".format(j), repr(line))

if i == 1:
    print("All is clear! ^__^")
    sys.exit(0)
else:
    sys.exit(1)
