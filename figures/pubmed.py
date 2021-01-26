#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv("PubMed_Timeline_Results_by_Year.csv", index_col=False, infer_datetime_format=True)
df = pd.read_csv("PubMed_Timeline_Results_by_Yearmetagenomics.csv", infer_datetime_format=True)
df.sort_values(['Year'], inplace=True)
'''
df.plot(kind="bar",
        x="Year",
        y="Count")
'''
plt.bar(df.Year, df.Count)
plt.xlabel("Year")
plt.ylabel("Paper Count")
#plt.show()
plt.savefig("popularity.png")
