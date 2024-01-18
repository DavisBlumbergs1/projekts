import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from PIL import Image

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url= "https://nodarbibas.rtu.lv/"
driver.get(url)
time.sleep(3)

find = driver.find_element(By.CLASS_NAME, "btn.dropdown-toggle.btn-light")
find.click()

find = driver.find_element(By.ID, "bs-select-1-9")
find.click()
time.sleep(0.1)

find = driver.find_element(By.ID, "course-id")
find.click()
find.send_keys("1")
find.send_keys(Keys.RETURN)
time.sleep(0.3)

find = driver.find_element(By.ID, "group-id")
find.click()
time.sleep(0.3)
find.send_keys("10")
find.send_keys(Keys.RETURN)
driver.maximize_window()






input()