from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 네이버 계정 정보 입력
NAVER_ID = "your_naver_id"
NAVER_PASSWORD = "your_password"

# ChromeDriver 경로 설정
chrome_driver_path = "/opt/homebrew/bin/python3"  # ChromeDriver 경로 설정

# WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  # 봇 탐지 방지
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # 네이버 로그인 페이지 접속
    driver.get("https://nid.naver.com/nidlogin.login")
    wait = WebDriverWait(driver, 10)

    # ID 입력
    id_input = wait.until(EC.presence_of_element_located((By.ID, "id")))
    id_input.click()
    id_input.send_keys(NAVER_ID)

    # 비밀번호 입력
    password_input = driver.find_element(By.ID, "pw")
    password_input.click()
    password_input.send_keys(NAVER_PASSWORD)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.ID, "log.login")
    login_button.click()

    # 로그인 후 대기
    time.sleep(5)
    
    # 이후 페이지 작업 가능

finally:
    # 브라우저 종료
    driver.quit()