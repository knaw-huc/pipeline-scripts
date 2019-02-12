# Extracts text from EAD files in the directory argv[1].
# All files with extension .xml are assumed to contain EAD records.
# Resulting text is in corresponding files with extension .txt in dir argv[2].

import os
from os.path import basename, join, splitext
import sys

from lxml import etree

NS = {'ead': 'urn:isbn:1-931666-22-9'}  # Namespace mapping for LXML

indir, outdir = sys.argv[1:]

os.makedirs(outdir, exist_ok=True)

for f in os.listdir(indir):
    base, ext = splitext(f)
    if ext != '.xml':
        continue

    outpath = os.path.join(outdir, base + '.txt')

    with open(outpath, 'w') as out:
        t = etree.parse(join(indir, f))
        txt = t.xpath('string(//ead:archdesc)', namespaces=NS)
        out.write(txt)
