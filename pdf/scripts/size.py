#!/usr/bin/env python
import pandas as pd
import sys
#The script's first argument is a csv file name that has been produced by the pdf parser. 
df = pd.read_csv(sys.argv[1],error_bad_lines=False, warn_bad_lines=True);
#If a row in csv has bad number of fields, a warning is generated and the row is dropped from the record. This typically happens when a 'comma' is encountered in the pdf file. Because 'comma' is used a separator as well in csv, this causes a confusion and csv row gets an extra field.

df['sizecount'] = 1;
sizegroup = df.groupby('size').sum()['sizecount'];
print("*********__", sys.argv[1],"__************");
print(sizegroup);
