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

time.sleep(1)

find = driver.find_element(By.XPATH, '//tbody[@role="presentation"]')
find.click()
driver.execute_script("window.scrollBy(0, 100);")
location = find.location
size = find.size

# time.sleep(1)
# scroll = driver.find_element(By.CSS_SELECTOR, "fc-scroller-harness fc-scroller-harness-liquid")
# scroll.execute_script("window.scrollBy(0, 100);")


element_height = size['height']
scroll_offset = 200  # You may need to adjust this value based on your page
num_screenshots = (element_height // scroll_offset) + 1

# Take a screenshot of the entire page
driver.save_screenshot('full_page_screenshot.png')

# Crop the screenshot to capture only the find
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

full_screenshot = Image.open('full_page_screenshot.png')

# Crop the image to the region of the element
element_screenshot = full_screenshot.crop((left, top, right, bottom))

# for i in range(num_screenshots):


# Save the cropped screenshot
element_screenshot.save('element_screenshot.png')


input()