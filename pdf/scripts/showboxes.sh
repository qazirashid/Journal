#!/usr/bin/env bash
#In the first step, pdfminer is used to convert the pdf file to xml file
pdf2txt.py  -t xml -A $1 > ${1}.xml
#In the second step, pass the pdf file and xml file to the draw.py
./draw.py $1 ${1}.xml

