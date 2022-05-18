import time
import os
import urllib.request
from urllib.parse import quote
from selenium import webdriver


word = input("검색할 단어 : ")
url = f"https://www.google.com/search?q={quote(word)}&tbm=isch&ved="
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

tags = driver.find_elements_by_class_name("rg_i")
time.sleep(1)

os.mkdir(f"{word}")
cnt = 1
time.sleep(1)

for tag in tags:
    if cnt == 3:
        break
    img = tag.get_attribute("src")
    urllib.request.urlretrieve(img, f"{word}//" + f"{word}{cnt}.jpg")
    cnt += 1
    time.sleep(2)










