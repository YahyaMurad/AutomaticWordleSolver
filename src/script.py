# Imports
import random
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

df = pd.read_csv("FreqWords.csv")

driver = webdriver.Chrome()
driver.get("https://www.nytimes.com/games/wordle/index.html")

sleep(2)

play_button = driver.find_element(By.XPATH, "(//button[@type='button'])[2]")
play_button.click()

sleep(2)

close_popup = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__TcEKb")
close_popup.click()

sleep(2)

words = ["notch"]

absent = []

present_chars = set()
present = []

correct_chars = set()
correct = []

count = {}
i = 0

while i < len(words):
    c = 0
    word = words[i]
    
    actions = ActionChains(driver)
    actions.send_keys(word, Keys.ENTER)
    actions.perform()
    
    sleep(2)

    for pos, l in enumerate(word):
        count[l] = 1 + count.get(l, 0)
        path = f"//div[text()='{l}']" if count[l] == 1 else f"(//div[text()='{l}'])[{count[l]}]"
        letter = driver.find_element(By.XPATH, path)
        state = letter.get_attribute("data-state")

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

    if c == 5:
        print("FINISHED")
        break
            
    sleep(2)


    for letter in absent:
        df = df[~df["FreqWords"].str.contains(letter)]

    for letter, position in present:
        df = df[df["FreqWords"].str.contains(letter)]
        df = df[df["FreqWords"].str[position] != letter]

    for letter, position in correct:
        df = df[df["FreqWords"].str[position] == letter]
    
    words.append(df["FreqWords"].iloc[0])
    
    i += 1
while True:
    pass