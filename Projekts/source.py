import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from PIL import Image
from io import BytesIO

#####IF IT DOESNT WORK##########
emergency_pause = 0

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url= "https://nodarbibas.rtu.lv/"
driver.get(url)
time.sleep(3)
time.sleep(emergency_pause)

find = driver.find_element(By.CLASS_NAME, "btn.dropdown-toggle.btn-light")
find.click()

find = driver.find_element(By.ID, "bs-select-1-9")
find.click()
time.sleep(0.1)
time.sleep(emergency_pause)

find = driver.find_element(By.ID, "course-id")
find.click()
find.send_keys("1")
find.send_keys(Keys.RETURN)
time.sleep(0.3)
time.sleep(emergency_pause)

find = driver.find_element(By.ID, "group-id")
time.sleep(emergency_pause)
find.click()
time.sleep(0.5)
time.sleep(emergency_pause)
find.send_keys("10")
find.send_keys(Keys.RETURN)
driver.maximize_window()

time.sleep(1)
time.sleep(emergency_pause)

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

# Create an empty image to store the stitched screenshots
stitched_image = Image.new('RGB', (full_screenshot.width, full_screenshot.height + (num_screenshots - 1) * scroll_offset))
time.sleep(emergency_pause)

# Paste the first screenshot
stitched_image.paste(full_screenshot, (0, 0))

# Scroll and capture screenshots
for i in range(1, num_screenshots):
    # Scroll the page
    driver.execute_script(f"window.scrollBy(0, {scroll_offset});")
    time.sleep(0.5)  # Adjust the sleep time if needed
    time.sleep(emergency_pause)

    # Take a screenshot of the current view
    screenshot_bytes = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot_bytes))

    # Paste the screenshot onto the stitched image
    stitched_image.paste(screenshot, (0, i * scroll_offset))

# Crop the stitched image to remove any extra white space
stitched_image = stitched_image.crop((left, 0, right, stitched_image.height))

# Save the final stitched image
stitched_image.save('stitched_screenshot.png')

driver.quit()



# input()