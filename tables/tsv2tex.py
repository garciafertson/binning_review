#!/usr/bin/env python3
import sys
import pandas as pd
'''
tsvfile = 'Table1_binning_software_since2017.tsv'
'''
tsvfile = sys.argv[1]
df = pd.read_csv(tsvfile, sep='\t')
print(df)
with pd.option_context("max_colwidth", 1000):
    df.to_latex(tsvfile + ".tex",index=False, column_format='p{2cm}|p{0.6cm}|p{4cm}|p{4cm}|p{3.4cm}')
