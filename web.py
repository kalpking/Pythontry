from selenium import webdriver

# Path to the ChromeDriver executable (update this with your ChromeDriver path)
chrome_driver_path = ""

# Create a new instance of the Chrome web driver
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")

# Open YouTube.com
driver.get("https://www.youtube.com")

# Close the browser window when you're done
driver.quit()
