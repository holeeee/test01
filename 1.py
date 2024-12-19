from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)

driver.find_element_by_css_selector('gLFyf').send_keys('python')