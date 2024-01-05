from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/chromedriver")
driver.implicitly_wait(2)
#driver.get("https://www.daum.net")

url = "https://www.linkedin.com/jobs/search/?currentJobId=3291207294&geoId=103588929&keywords=PYTHON&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%84%9C%EC%9A%B8&refresh=true"
driver.get(url)

login = driver.find_element(By.CSS_SELECTOR, ".btn-secondary-emphasis")
login.click()

username = driver.find_element(By.ID, "username")
username.send_keys("taewrui07@konkuk.ac.kr")

password = driver.find_element(By.ID, "password")
password.send_keys("0503tae**&")

login_button = driver.find_element(By.CSS_SELECTOR, ".from__button--floating")
login_button.click()

