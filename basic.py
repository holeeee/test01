from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://naver.com"

driver.get(url)

time.sleep(2)
'''
<input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">
'''
driver.find_element(By.NAME, "query").send_keys("이성호")
time.sleep(1)

driver.find_element(By.CLASS_NAME, "search_input").send_keys("장유정")

# CSS_SELECTOR "#xxxx"  /  CLASS_NAME ".xxxx"  class_name  앞에 . 안찍어야 동작함