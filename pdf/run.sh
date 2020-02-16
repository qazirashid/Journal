#!/usr/bin/env bash
pdf2txt.py -t xml -A $1 | grep text\ |\
tr -d '\"/' | tr '=<>' ' '|\
awk 'BEGIN{FS=" ";OFS="," ;print "font,size,y1,y2,x1,x2,char"}
     	{ split($5,position,",");
	 print $3,$7,position[2],position[4],position[1], position[3],$8 }'|\
awk -F, 'NF==7{print $0}' > $2
