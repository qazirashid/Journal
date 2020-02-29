#!/usr/bin/env python

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import sys

fp = open(sys.argv[1],'rb');
parser = PDFParser(fp)
document = PDFDocument(parser,'')
outlines = document.get_outlines()
for (level, title, dest, a , se) in outlines:
	print (level,title)
