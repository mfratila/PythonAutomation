
import os
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()
driver.get('https://trovo.live/hideincocioc')
# driver.maximize_window()
driver.implicitly_wait(8)
time.sleep(2)

logPopup_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/nav/div[3]/div[3]/button')
logPopup_element.click()
time.sleep(1)
email_element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[1]/div/input')
pass_element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[3]/div/input')
loginButton_element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/button')
email_element.send_keys('YOUR EMAIL ADDRESS')
pass_element.send_keys('YOUR PASSWORD')
loginButton_element.click()
time.sleep(3)
followButton_element = driver.find_element(By.XPATH, '//*[@id="live-fullscreen"]/div[3]/div[3]/section/div[2]/button[3]')
followButton_element.click()
