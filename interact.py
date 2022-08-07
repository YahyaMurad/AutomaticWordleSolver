from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.nytimes.com/games/wordle/index.html")

driver.implicitly_wait(10)


close = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__b4z74")
close.click()


words = ["notch", "right", "slank", "stick"]


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

for t in range(6):
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

        if state == "included":
            included.append(inner)
        elif state == "absent":
            excluded.append(inner)
        elif state == "correct":
            positions[i % 5] = inner


    print(included)
    print(excluded)
    print(positions)

    start = end
    end = end + 5
    num += 1
    ind += 1

datastates = ["absent", "present", "correct", "empty"]

