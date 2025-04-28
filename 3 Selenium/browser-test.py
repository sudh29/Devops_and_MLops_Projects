from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Selenium Grid / Remote WebDriver server
server_url = "http://127.0.0.1:4444/wd/hub"

# Configure Firefox options
options = Options()
options.headless = True  # run in headless mode

# Point to the GeckoDriver service (not strictly needed if geckodriver is in PATH)
service = Service()

# Create remote WebDriver session
driver = webdriver.Remote(
    command_executor=server_url,
    options=options,
    service=service
)

print("Loading page...")
driver.get("https://fedoramagazine.org/")
print("Loaded:", driver.title)

assert "Fedora" in driver.title
driver.quit()
print("Done.")
