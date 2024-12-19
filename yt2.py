from selenium import webdriver  '''-- 필수'''
# send__key 위해서
from selenium.webdriver.common.by import By  '''-- 필수'''
from selenium.webdriver.chrome.options import Options
# 엔터 입력을 위해서
from selenium.webdriver.common.keys import Keys
import time

#options 변수 생성
options = Options()
options.add_argument("--start-maximized")
#화면 안꺼지는 옵션
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(3)

# query = driver.find_element(By.ID, "query").send_keys("인공지능")도 가능
query = driver.find_element(By.ID, "query")
query.send_keys("인공지능")
time.sleep(2)

''' 검색 버튼 클릭
search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")
search_btn.click()
'''

query = driver.find_element(By.ID, "query").send_keys(Keys.ENTER)

time.sleep(2)
driver.save_screenshot("네이버_인공지능.png")
driver.quit()