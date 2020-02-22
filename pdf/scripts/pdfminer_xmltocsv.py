#!/usr/bin/env python
import pandas as pd
import xml.etree.ElementTree as et
import sys

# The hierarchy of xml to be parsed.
elem_list=['page','textbox','textline','text']
xmlfile = sys.argv[1];

xtree = et.parse(xmlfile);

pages = xtree.getroot();

col_names=["page","txtbox","textline","font","szie", "x1","y1","x2","y2","char"]
str_cols = ','.join(map(str,col_names))
print(str_cols);
textlineid=0;
rows = [];
for page in pages:
  pageid=page.attrib.get("id")
  textlineid=0;
  for tbox in page.findall("textbox"):
    tboxid=tbox.attrib.get("id")
    for textline in tbox.findall("textline"):
      textlineid +=1
      for char in textline.findall("text"):
        bbox=char.attrib.get("bbox")
        font=char.attrib.get("font")
        size=char.attrib.get("size")
        charval=char.text
        if font is not None and size is not None and bbox is not None:
          if (charval==","):
            charval=":"
          print(pageid,",",tboxid,",",textlineid,",",font,",",size,",",bbox,",",charval,sep='')

 
