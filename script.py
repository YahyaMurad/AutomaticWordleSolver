import pandas as pd

df = pd.read_csv('FreqWords.csv')

df['FreqWords'].str.lower()
df.drop_duplicates()

# df = pd.read_csv('words.csv')
one = ""
pd.set_option('display.max_rows', None)
while one != "OUT":
    excludedChars = input("Type all excluded chars without separation: ")
    includedChars = input("Type all included chars without separation: ")
    one = input("First Letter: ")
    two = input("Second Letter: ")
    thr = input("Third Letter: ")
    fou = input("Fourth Letter: ")
    fiv = input("Fifth Letter: ")

    #[\w][\w][\w][\w][\w]
    #[\w]{5}
    #[abcdefghijklmnopqwxyz][\w][t][h][d]
    #[0-9]|[d-j]
    # ^(?!.*[mghtlc])(?=.*i)(?=.*o)(?=.*s).*

    one = one if one != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    two = two if two != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    thr = thr if thr != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    fou = fou if fou != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    fiv = fiv if fiv != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    six =

    df["FreqWords"] = df["FreqWords"].str.extract("(^" + one + two + thr + fou + fiv + ")", expand=True)

    for i in includedChars:
        df["FreqWords"] = df["FreqWords"].str.extract("(.*[" + i + "].*)", expand=True)

    print(df[df["FreqWords"].notnull() == True])
