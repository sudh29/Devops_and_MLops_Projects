from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Choose the browser: 'chrome', 'firefox', or 'edge'
browser_name = os.getenv("BROWSER", "chrome").lower()

# URL of the Selenium Grid (not the UI)
grid_url = 'http://localhost:4444/wd/hub'

# Select browser options and driver
if browser_name == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--headless')  # Uncomment for headless
    driver = webdriver.Remote(command_executor=grid_url, options=options)

elif browser_name == "firefox":
    options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')  # Uncomment for headless
    driver = webdriver.Remote(command_executor=grid_url, options=options)

elif browser_name == "edge":
    options = webdriver.EdgeOptions()
    # options.add_argument('--headless')  # Uncomment for headless
    driver = webdriver.Remote(command_executor=grid_url, options=options)

else:
    raise ValueError(f"Unsupported browser: {browser_name}")

try:
    # Open Google
    driver.get("https://www.google.com")
    print("Page title is:", driver.title)

    time.sleep(2)

    # Perform a search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Podman Selenium Test")
    search_box.submit()

    time.sleep(20)
    print("New page title is:", driver.title)

finally:
    driver.quit()
