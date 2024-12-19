# webdriver 가져와
from selenium import webdriver
# web driver
from webdriver_manager.chrome import ChromeDriverManager
#브라우저 꺼짐 방지 옵션
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 브라우저 꺼짐 방지 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ChromeDriver 서비스 객체 생성
service = Service(ChromeDriverManager().install())

# WebDriver 초기화
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL 열기
url = 'https://google.com'
driver.get(url)
