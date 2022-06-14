import time
import os
import urllib.request
from urllib.parse import quote
from selenium import webdriver

# 403 에러 방지용, 해당 크롬드라이버버전 맞춰서 있어야 합니다.
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

# 크롬 드라이버 구동
word = input("크롤링할 웹툰 이름을 적어주세요 : ")
url = f"https://comic.naver.com/search?keyword={word}"
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
time.sleep(0.2)

# 본 웹툰 크롤링
driver.find_element_by_css_selector(
    "#content > div:nth-child(2) > ul > li > h5 > a").click()
time.sleep(0.2)
driver.find_element_by_css_selector(
    "#content > table > tbody > tr:nth-child(3) > td:nth-child(1) > a > span").click()
driver.find_element_by_css_selector(
    "#comicRemocon > div.remote_cont > div.btn_area > a.btn_prev_end").click()
time.sleep(0.2)

# 폴더 만들기
os.mkdir(f"{word}")
time.sleep(0.2)

# 컷신 수
cnt = 0
# 몇화
total = 1

while True:
    try:
        tag = driver.find_element_by_css_selector(f"#content_image_{cnt}")
        img = tag.get_attribute("src")
        urllib.request.urlretrieve(
            img, f"{word}//" + f"{word} {total}화 {cnt}.jpg")
        cnt += 1
        time.sleep(0.2)
    except:
        driver.find_element_by_css_selector(
            f"#comicRemocon > div.remote_cont > div.btn_area > a.btn_next").click()
        cnt = 0
        total += 1
        time.sleep(0.2)


print("이미지 크롤링 완료")
