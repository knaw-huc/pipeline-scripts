# Runs frog on all files in argv[1] to produce NER'd FoLiA-format output
# in the dir argv[2]. A log is kept in frog.log.
# This uses the LaMachine Docker image.
#
# An example run on 1MB's worth of EAD records (142 files) took 21m14s
# and produced 43.8MB of FoLiA output.

import os
from os.path import abspath
import subprocess
import sys

inputdir, outputdir = map(abspath, sys.argv[1:])

os.makedirs(outputdir, exist_ok=True)

with open('frog.log', 'a') as log, open('/dev/null', 'w') as null:
    subprocess.call(["docker", "run",
                     # inputdir as /in, read-only volume
                     "-v", "%s:/in:ro" % inputdir,
                     # outputdir as /out, read-write volume
                     "-v", "%s:/out" % outputdir,
                     "proycon/lamachine", "frog",
                     "--skip=mptcla",
                     "--testdir=/in", "--xmldir=/out"],
                    stderr=log, stdout=null)
