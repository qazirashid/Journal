#!/usr/bin/env bash

# convert the pdf to a png. Remove the alpha channel.
# Resize the image to A4 page, which pdf takes as 595x842 points. 
# Each pdf point is presented as a pixel in the output image.

# each page is imaged in a sepearte file.
convert $1 -resize 595x842 ${2}_%02d.png  
