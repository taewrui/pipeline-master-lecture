from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/User/Desktop/Chromedriver.exe")
driver.implicitly_wait(2)
driver.get("https://www.daum.net")