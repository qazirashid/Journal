#!/usr/bin/env python

import sys
#from PIL import Image, ImageDraw
from wand.image import Image as wi 
import xml.etree.ElementTree as et
from wand.drawing import Drawing
from wand.color import Color
# The script expect to be called only from a bash script which has already called pdf2txt on the file.pdf [passed as argument] and has created a file.pdf.xml. 

def drawRect(img,bbox,color, sw):
	slist = bbox.split(",")
	rlist= [float(x) for x in slist];
	ys = img.size[1];
	xl = rlist.copy()
	xl[1] = ys - rlist[3]
	xl[3] = ys - rlist[1]
	with Drawing() as draw:
		draw.fill_opacity=0;
		draw.stroke_width=sw;
		draw.stroke_color=color;
		print("draw rect:",xl[0], xl[1], xl[2],xl[3])
		draw.rectangle(left=xl[0],top=xl[1],right=xl[2], bottom=xl[3])
		draw(img)
		return img
xmlfile = sys.argv[2] 
#Obtain the xml tree for pdf file
xmltree = et.parse(xmlfile)
pages = xmltree.getroot()
# pdf file is given to ImageMagick for conversion to image files.
# Each pdf page is converted to an image. The pdf file yeidls a list of images, one image per page.

images = wi(filename=sys.argv[1])
for index,ims in enumerate(images.sequence):
	#Prepare the image.
	img=wi(ims)
	#Trun off alpha channel
	img.alpha_channel='remove'
	xs = img.size[0]; ys = img.size[1];
	#Get the current page from xml file.
	xmlpage=pages[index]
	layout = xmlpage.find('layout')
	for textgroup in list(layout.iter('textgroup')):
		for tbox in list(textgroup.iter('textbox')):
			tbox = tbox.attrib.get("bbox")
			print("calling rect:", tbox)
			img = drawRect(img, tbox, Color('red'),3)
		tgbox=textgroup.attrib.get("bbox")
		img = drawRect(img,tgbox, Color('blue'),1)
		print(index,"--",tgbox)
	img.save(filename=sys.argv[1] + "_" + str(index) +".png") 
	print(img.size)


		

 
