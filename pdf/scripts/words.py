#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys

space_th = 1 ; # space threshold
# dfr is the data frame of chars as created by pdfminer
dfr = pd.read_csv(sys.argv[1])
#df is the sorted version of dfr. The sorting brings the words in the correct order. 
df = dfr.sort_values(by=['page','txtbox', 'y2','x1'], ascending=[True,True, False, True])
# The index of df is still inherited from dfr which as become unusable for later algorithms because of sorting. So we rest index to ensure that frames in df are ordered by a monotonically increasing index.

df.reset_index(drop=True, inplace=True);
#Debug step. remove if no issues are found.
#sname = sys.argv[2] + ".s.csv";
#df.to_csv(sname);
#debug end

# calculate inter-character space
xspace = np.roll(df['x1'],-1) - df['x2'];
yspace = np.roll(df['y1'],-1) - df['y1'];
# calculate word boundaries
wb = xspace.abs() > space_th

df['xspace'] = xspace;
df['yspace'] = yspace;
df['concat'] = df['xspace'].abs() < space_th;
i = 0; ix=0;
num_records = df.shape[0];
words = df['char'].copy();
wx1 = df['x1'].copy();

#If a group of characters has distance between characters less than a threshold, then assemble those characters in words.

while(i<num_records):
  charsum=df.iloc[i].char
  ix=i;
  while(df.iloc[i].concat):
    i=i+1
    if (i >= num_records):
      continue;
    charsum = charsum + df.iloc[i].char
  words[i] = charsum;
  wx1[i] = wx1[ix]; 
  #This updates the boudning box of word to include all charcaters grouped together 
  i = i + 1

df['words'] = words;
df['wx1']  = wx1;
df['wb'] = wb

#df.to_csv(sys.argv[2] + ".w.csv")

# drop partial words and keep complete words only
dw = df[df['wb']]
#drop unwanted columns to declutter the csv.
dw= dw.drop(columns=['x1', 'char','concat', 'wb'])
dw.to_csv(sys.argv[2])


    
