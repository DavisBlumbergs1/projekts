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
time.sleep(0.5)
find.send_keys("10")
find.send_keys(Keys.RETURN)
driver.maximize_window()

time.sleep(1)

find = driver.find_element(By.XPATH, '//tbody[@role="presentation"]')
driver.execute_script("window.scrollBy(0, 300);")
location = find.location
size = find.size








element_height = size['height']
scroll_offset = 300  # You may need to adjust this value based on your page
num_screenshots = (element_height // scroll_offset) + 1
print(num_screenshots)

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


for i in range(num_screenshots):



# for i in range(num_screenshots):
#     # Calculate the scroll distance
#     scroll_distance = i * scroll_offset
#     driver.execute_script(f"window.scrollTo(0, {scroll_distance});")

#     # Take a screenshot of the visible area
#     screenshot_filename = f'screenshot_{i}.png'
#     driver.save_screenshot(screenshot_filename)
#     screenshot = Image.open(screenshot_filename)

#     # Paste the screenshot into the full screenshot
#     full_screenshot.paste(screenshot, (0, i * scroll_offset))

#     # Delete the temporary screenshot file
#     screenshot.close()
#     os.remove(screenshot_filename)


# Save the cropped screenshot
element_screenshot.save('element_screenshot.png')








input()