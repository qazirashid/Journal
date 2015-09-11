#!/usr/bin/env python
import sys
import zlib
import hashlib
if(len(sys.argv) < 2):
    print "No object path to dump"
    exit(-1);
try:
    with open(sys.argv[1], 'r') as f:
        zcontent = f.read();
except:
    sys.exit("ERROR: Could not open the specified object");

content = zlib.decompress(zcontent);
print content
