from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Loading dataset
df = pd.read_csv("FreqWords.csv")

# Initializing driver
driver = webdriver.Chrome()  # Add driver path
driver.get("https://www.nytimes.com/games/wordle/index.html")

sleep(2)

# Find and click the play button
play_button = driver.find_element(By.XPATH, "(//button[@type='button'])[2]")
play_button.click()

sleep(2)

# Close instructions pop up
close_popup = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__TcEKb")
close_popup.click()

sleep(2)

# Starting word
words = ["trace"]

# Variables to store absent, present, and correct chars
absent = []

present_chars = set()
present = []  # Stores indices

correct_chars = set()
correct = []  # Stores indices

count = {}  # Dictionary to keep track of count of chars (Used to target elements)
i = 0

while i < len(words):
    c = 0  # Keep track of the correct letters
    word = words[i]

    # Write the word
    actions = ActionChains(driver)
    actions.send_keys(word, Keys.ENTER)
    actions.perform()

    sleep(2)

    # Check every character
    for pos, l in enumerate(word):
        count[l] = 1 + count.get(l, 0)  # Increment count
        path = (
            f"//div[text()='{l}']"
            if count[l] == 1
            else f"(//div[text()='{l}'])[{count[l]}]"
        )
        letter = driver.find_element(By.XPATH, path)  # Letter
        state = letter.get_attribute(
            "data-state"
        )  # State of the letter (absent, present, correct)

        # Add letter to corresponding array/set
        if state == "absent":
            if l not in present_chars and l not in correct_chars:
                absent.append(l)
        elif state == "present":
            present.append((l, pos))
            present_chars.add(l)
        elif state == "correct":
            c += 1
            correct.append((l, pos))
            correct_chars.add(l)

    # If 5 correct letters (Correct word guessed)
    if c == 5:
        print("FINISHED")
        break

    sleep(2)

    # Updating dataset
    for letter in absent:
        df = df[~df["FreqWords"].str.contains(letter)]

    for letter, position in present:
        df = df[df["FreqWords"].str.contains(letter)]
        df = df[df["FreqWords"].str[position] != letter]

    for letter, position in correct:
        df = df[df["FreqWords"].str[position] == letter]

    # Add the first word from the dataset to the list of words
    words.append(df["FreqWords"].iloc[0])

    i += 1

sleep(3)
