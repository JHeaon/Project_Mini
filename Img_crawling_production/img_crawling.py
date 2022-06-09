import time
import os
import urllib.request
from urllib.parse import quote
from selenium import webdriver

# 403 에러 방지
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


word = input("검색할 단어 : ")
url = f"https://www.google.com/search?q={quote(word)}&tbm=isch&ved="
driver = webdriver.Chrome("Img_crawling\chromedriver.exe")
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
