#!/usr/bin/env python
# This script will mark words that show possiblity of being in a table.
# input is a csv file with words extracted using 'pdftocsv.sh'.
# The output is another csv with more columns that are useful for detecting tables.

import pandas as pd
import numpy as np
import sys

df = pd.read_csv(sys.argv[1])
# Mark line breaks
linebreak = (df['yspace'] < 0).replace({True:1, False:0});
df['linebreak'] = linebreak;
#udw will inicate unusual distance between two words
#ud_th is the threshold for flagging the distance as unusual
ud_th = 5;
udw = (df['xspace']> ud_th).replace({True:1, False:0});
df['udw'] = udw;

# next we check whether a word is the first word on a line

fwol = np.roll(linebreak,1);
fwol[0] = 1;

# We check the distance of first word from the right margin.
# We limit it to only thos words that are first on their line.
drm = df['wx1']*fwol;
#next define a threshold that check whether drm is normal. 
# To be calculated later. 
drm_th = 150; 
udrm = (drm > drm_th).replace({True:1, False:0})
df['udrm'] = udrm;

tc = udw+udrm;
df['tc'] = tc;
g = df.groupby(['y2','page']).sum();
g = g.sort_values(by=['page','y2'],ascending=[True,False])

gf= g['tc'];

df.to_csv(sys.argv[2])
gf.to_csv(sys.argv[2] + ".tablecandidates.csv")




 





