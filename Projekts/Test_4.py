from selenium import webdriver
from PIL import Image

# Set the path to the WebDriver executable
webdriver_path = 'path/to/chromedriver'  # Update this with the path to your WebDriver

# Initialize the WebDriver (in this case, Chrome)
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the URL of the page containing the element
url = 'https://example.com'
driver.get(url)

# Find the element you want to capture
element = driver.find_element_by_css_selector('your_element_selector')
# Replace 'your_element_selector' with the actual CSS selector of the element you want to capture

# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Get the location and size of the element
location = element.location
size = element.size

# Calculate the number of screenshots needed based on the element's height
element_height = size['height']
scroll_offset = 200  # You may need to adjust this value based on your page
num_screenshots = (element_height // scroll_offset) + 1

# Take multiple screenshots and stitch them together
full_screenshot = Image.new('RGB', (size['width'], element_height))

for i in range(num_screenshots):
    # Calculate the scroll distance
    scroll_distance = i * scroll_offset
    driver.execute_script(f"window.scrollTo(0, {scroll_distance});")

    # Take a screenshot of the visible area
    screenshot_filename = f'screenshot_{i}.png'
    driver.save_screenshot(screenshot_filename)
    screenshot = Image.open(screenshot_filename)

    # Paste the screenshot into the full screenshot
    full_screenshot.paste(screenshot, (0, i * scroll_offset))

    # Delete the temporary screenshot file
    screenshot.close()
    os.remove(screenshot_filename)

# Save the stitched screenshot
full_screenshot.save('element_screenshot.png')

# Close the browser
driver.quit()
