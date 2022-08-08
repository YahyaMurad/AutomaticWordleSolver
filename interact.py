# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pandas as pd
import random

df = pd.read_csv('FreqWords.csv')

df['FreqWords'].str.lower()
df.drop_duplicates()


PATH = "chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.nytimes.com/games/wordle/index.html")

driver.implicitly_wait(10)


close = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__b4z74")
close.click()


words = ["notch"]


ind = 0
num = 1
start = 0
end = 5

included = []
excluded = []
positions = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0 
}

for t in range(1000):
    word = words[ind]
    for s in word:
        but = driver.find_element(By.XPATH, "//button[@data-key=\"" + s + "\"]")
        but.click()

    submit = driver.find_element(By.XPATH, "//button[@data-key=\"↵\"]")
    submit.click()

    
    time.sleep(2)

    a = driver.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")
    
    for i in range(start, end):
        n = a[i]
        inner = n.get_attribute("innerHTML")
        state = n.get_attribute("data-state")

        if state == "present":
            included.append(inner)
        elif state == "absent":
            excluded.append(inner)
        elif state == "correct":
            positions[i % 5] = inner


    includedChars = included
    excludedChars = excluded

    one = "" if positions[0] == 0 else positions[0]
    two = "" if positions[1] == 0 else positions[1]
    thr = "" if positions[2] == 0 else positions[2]
    fou = "" if positions[3] == 0 else positions[3]
    fiv = "" if positions[4] == 0 else positions[4]

    one = one if one != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    two = two if two != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    thr = thr if thr != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    fou = fou if fou != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
    fiv = fiv if fiv != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")

    print(includedChars)
    print(excludedChars)
    print(one)
    print(two)
    print(thr)
    print(fou)
    print(fiv)

    df["FreqWords"] = df["FreqWords"].str.extract("(^" + one + two + thr + fou + fiv + ")", expand=True)
    
    for i in includedChars:
        df["FreqWords"] = df["FreqWords"].str.extract("(.*[" + i + "].*)", expand=True)

    print(includedChars)
    print(excludedChars)
    print(one)
    print(two)
    print(thr)
    print(fou)
    print(fiv)

    df = df[df["FreqWords"].notnull() == True]
    print(df)
    r = random.randint(0, len(df)-1)
    print(df.iloc[r]["FreqWords"])
    words.append(df.iloc[r]["FreqWords"].lower())

    start = end
    end = end + 5
    num += 1
    ind += 1