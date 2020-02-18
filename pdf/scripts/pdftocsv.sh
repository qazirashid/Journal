#!/usr/bin/env bash
#usage:  ./pdftocsv.sh pathtopdf/filename.pdf  pathtosv/filename
#Note, the "," gets replaced by ":" in the csv to avoid error. This is temporary fix.
pdf2txt.py -t xml -A $1 > $2.xml
./pdfminer_xmltocsv.py $2.xml > $2.csv 
