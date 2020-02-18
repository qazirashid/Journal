#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys

df = read_csv(sys.argv[1])

xspace = np.roll(df['x2'],-1) - df['x1'];
yspace = np.roll(df['y1'],-1) - df['y1'];
# calculate word boundaries
wb = xspace.abs() > 1;


