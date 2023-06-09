import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.INFO)

hub_url = "http://Selenium_Container:4444/wd/hub"

# Create a new instance of the Chrome driver
chrome_options = Options()
chrome_options.add_argument('--browserName=chrome')

driver = webdriver.Remote(command_executor=hub_url, options=chrome_options)

try:
    # Get the Google homepage
    driver.get("https://www.google.com")

    title = driver.title
    logging.info(f"Python-1 Project says: Search results page title: {title}")

    # Capture a screenshot
    screenshot_path = "T-HEX/Screenshot1.png"
    driver.save_screenshot(screenshot_path)
    logging.info(f"Screenshot saved: {screenshot_path}")

    

finally:
    driver.quit()