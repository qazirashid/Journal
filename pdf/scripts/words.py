#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys

space_th = 1 ; # space threshold
dfr = pd.read_csv(sys.argv[1])
df = dfr.sort_values(by=['y2','x1'], ascending=[False, True])
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

dw = df[df['wb']]
dw= dw.drop(columns=['x1', 'char','concat', 'wb'])
dw.to_csv(sys.argv[2])


    
