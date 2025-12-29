#!/usr/bin/env python3

# this is a base script for installing the app, adding --break-system-packages on pip versions where it's called for
# you can add your own stuff into this script!
# please consider making it clear to the user what is being done

from packaging.version import Version
from subprocess import check_output
import os
import sys

flag_filename = ".installed"

if os.path.exists(flag_filename):
    print("Already installed; remove '{}' to run the install process again".format(flag_filename))
    sys.exit(1)

cmdline = ["python3", "-m", "pip", "install"]

# checking pip version to see if we need --break-system-packages
output = check_output(["pip", "--version"])
if isinstance(output, bytes): output = output.decode("utf-8")
_, ver, _ = output.split(' ', 2)
if Version(ver) > Version("23.0.0"):
    cmdline.append("--break-system-packages")

cmdline.append("--editable")
cmdline.append(".")

print("Running:", " ".join(cmdline))
check_output(cmdline)

with open(flag_filename, "a") as f:
    pass
