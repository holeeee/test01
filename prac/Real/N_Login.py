from selenium import webdriver
from selenium.webdriver.common.by import By  #
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains #마우스 이동, 키보드 입력 등 사용자 동작을 시뮬레이션 하는데 사용.
from selenium.webdriver.common.keys import Keys # 키보드 입력 위해
import pyperclip #네이버 로그인 시 챕챠 뜨는거 방지위해 pyperclip 라이브러리 사용

options = Options()
options.add_experimental_option("detach", True) # 화면 안꺼지게하는 옵션
options.add_argument("--start-maximized") # 화면 최대화
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://naver.com"

#url 호출
driver.get(url)
time.sleep(2)

#로그인 화면 이동위해 로그인 버튼 클릭
search_btn = driver.find_element(By.ID, "account").click()
time.sleep(2)

#ID 입력
# driver.find_element(By.NAME, "id").send_keys("shwaplqa")  기존 코드
id_input = driver.find_element(By.NAME,"id")
id_input.click()
pyperclip.copy("shwaplqa")
actions = ActionChains(driver)
actions.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(1)

#PWD 입력
#driver.find_element(By.NAME, "pw").send_keys("waplqa!@")  기존코드
id_input = driver.find_element(By.NAME,"pw")
id_input.click()
pyperclip.copy("waplqa!@")
actions = ActionChains(driver)
actions.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(1)

#로그인 버튼 클릭
search_btn = driver.find_element(By.ID, "log.login.text").click()
time.sleep(2)

#메인 홈페이지에서 블로그 클릭  = driver.find_element(By.CLASS_NAME,"service_icon.type_blog").send_keys(Keys.Enter) 이렇게 키보드 입력으로 작성 가능
blog_btn = driver.find_element(By.CLASS_NAME,"service_icon.type_blog")
blog_btn.click()

'''
<input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">
'''
'''
#검색창에 이성호 입력
driver.find_element(By.NAME, "query").send_keys("이성호")
time.sleep(1)

driver.find_element(By.CLASS_NAME, "search_input").send_keys("장유정")
'''

# CSS_SELECTOR "#xxxx"  /  CLASS_NAME ".xxxx"  class_name  앞에 . 안찍어야 동작함

'''
## query = driver.find_element(By.ID, "query").send_keys("인공지능")도 가능
query = driver.find_element(By.ID, "query")
query.send_keys("인공지능")
time.sleep(2)
'''

'''
# 검색 버튼 클릭
search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")
search_btn.click()
'''
#스크린샷
#driver.saver_screenshot("shot_1.png")

# zzz

# driver quit