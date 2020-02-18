#!/usr/bin/env bash

#usage:  ./fontanalysis.sh filename.pdf
#note. Depends on pdftocsv.sh and size.py

./pdftocsv.sh $1 ${1}.csv
./size.py ${1}.csv

