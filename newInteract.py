# Imports
import time
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Dataset
df = pd.read_csv('FreqWords.csv')
df.drop_duplicates()


# Driver
PATH = "chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://www.nytimes.com/games/wordle/index.html")

driver.implicitly_wait(10)

# Close information popup
close = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__b4z74")
close.click()

# List of words to be used
words = ["notch"]

# Important variables
includedChars = []
excludedChars = []

positions = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0 
}
excludedPositions = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

# Counters and such
ind = 0
start = 0
end = 5

deleting = False

while True:
    # Get word
    word = words[ind]

    # Type word
    for s in word:
        but = driver.find_element(By.XPATH, "//button[@data-key=\"" + s + "\"]")
        but.click()

    # Press enter
    submit = driver.find_element(By.XPATH, "//button[@data-key=\"↵\"]")
    submit.click()

    time.sleep(2)

    
    letters = driver.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")
    state = letters[0].get_attribute("data-state")

    if state == "tbd" and deleting:
        delete = driver.find_element(By.XPATH, "//button[@data-key=\"←\"]")
        time.sleep(2)
        driver.implicitly_wait(10)

        delete.click()
        delete.click()
        delete.click()
        delete.click()
        delete.click()
        driver.implicitly_wait(10)

        deleting = False
        words.pop()
    else:
        # Check state of all letters
        for i in range(start, end):
            letter = letters[i]
            innerHTML = letter.get_attribute("innerHTML")
            state = letter.get_attribute("data-state")

            if state == "present":
                includedChars.append(innerHTML)
                excludedPositions[i % 5] = innerHTML
            elif state == "absent":
                excludedChars.append(innerHTML)
            elif state == "correct":
                positions[i % 5] = innerHTML

        # Initialize positions if known
        one = "" if positions[0] == 0 else positions[0]
        two = "" if positions[1] == 0 else positions[1]
        thr = "" if positions[2] == 0 else positions[2]
        fou = "" if positions[3] == 0 else positions[3]
        fiv = "" if positions[4] == 0 else positions[4]

        # Initialize excluded positions if known
        one = one if one != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
        two = two if two != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
        thr = thr if thr != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
        fou = fou if fou != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")
        fiv = fiv if fiv != "" else ("[^" + "".join(excludedChars) + "]" if excludedChars != "" else ".")


        print(includedChars)
        print(excludedChars)
        print(excludedPositions)
        print(one)
        print(two)
        print(thr)
        print(fou)
        print(fiv)


        # Extract words containing excluded characters
        df["FreqWords"] = df["FreqWords"].str.extract("(^" + one + two + thr + fou + fiv + ")", expand=True)

        # Extract words containing included characters
        for i in includedChars:
            df["FreqWords"] = df["FreqWords"].str.extract("(.*[" + i + "].*)", expand=True)

        # Randomly guess a word
        df = df[df["FreqWords"].notnull() == True]
        print(df)
        r = random.randint(0, len(df)-1)
        print(df.iloc[r]["FreqWords"])
        words.append(df.iloc[r]["FreqWords"].lower())

        # Update counters
        start = end
        end = end + 5
        ind += 1
        deleting = True