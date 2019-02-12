# Runs frog on all files in argv[1] to produce NER'd FoLiA-format output
# in the dir argv[2]. A log is kept in frog.log.
# This uses the LaMachine Docker image.

import os
from os.path import abspath
import subprocess
import sys

inputdir, outputdir = map(abspath, sys.argv[1:])

os.makedirs(outputdir, exist_ok=True)

with open('/dev/null', 'w') as null:
    subprocess.call(["frog", "--skip=mptcla",
                     "--testdir=/text", "--xmldir=/folia"],
                    stdout=null)
