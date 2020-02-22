#!/usr/bin/env bash
#usage:  ./pdftocsv.sh pathtopdf/filename.pdf  pathtosv/filename
#Note, the "," gets replaced by ":" in the csv to avoid error. This is temporary fix.
pdf2txt.py -t xml -A $1 > $1.xml
./pdfminer_xmltocsv.py $1.xml > $1.csv
./words.py $1.csv $2 
