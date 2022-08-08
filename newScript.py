import pandas as pd
import string
import random 

df = pd.read_csv('FreqWords.csv')

df['FreqWords'].str.lower()
df.drop_duplicates()

includedChars = []
excludedChars = []
notExcluded = []
one = ""
while True:
    exc = list(input("Type all excluded chars without separation: "))
    if len(exc) != 0:
        excludedChars.extend(exc)

    inc = list(input("Type all included chars without separation: "))
    if len(inc) != 0:
        includedChars.extend(inc)

    notExcluded = [x for x in string.ascii_lowercase if x not in excludedChars]

    one = input("First Letter: ")
    two = input("Second Letter: ")
    thr = input("Third Letter: ")
    fou = input("Fourth Letter: ")
    fiv = input("Fifth Letter: ")
    
    # print(excludedChars)
    # print(includedChars)

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