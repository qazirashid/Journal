#!/usr/bin/env sh
find .git/objects -type f | xargs -n 1 ./dumpobject.py
