#!/usr/bin/env bash
pdf2txt.py -t xml -A ./sample/hello.pdf | grep text\ |\
tr -d '\"/' | tr '=<>' ' '|\
awk 'BEGIN{FS=" ";OFS="|" ;print "font,size, x1,x2,y1,y2,char"}
     	{ split($5,position,",");
	 print $3,$7,position[2],position[4],position[1], position[3],$8 }'
