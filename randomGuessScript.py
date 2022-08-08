import pandas as pd
import random

df = pd.read_csv('FreqWords.csv')

df['FreqWords'].str.lower()
df.drop_duplicates()

includedChars = []
excludedChars = []

one = ""
two = ""
thr = ""
fou = ""
fiv = ""

one = one if one != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
two = two if two != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
thr = thr if thr != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
fou = fou if fou != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
fiv = fiv if fiv != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")

df["FreqWords"] = df["FreqWords"].str.extract("(^" + one + two + thr + fou + fiv + ")", expand=True)
for i in includedChars:
    df["FreqWords"] = df["FreqWords"].str.extract("(.*[" + i + "].*)", expand=True)

df = df[df["FreqWords"].notnull() == True]
r = random.randint(0, len(df)-1)
print(df.iloc[r])