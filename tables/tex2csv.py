#!/usr/bin/env python3
import sys
import pandas as pd
df = pd.read_csv(sys.argv[1], sep='\t')
print(df)
df.to_latex(sys.argv[1] + ".tex",index=False)
