# Import time module, since we want the wait 5 seconds before closing the browser
import time
# Import web driver from selenium
from selenium import webdriver

# Following is the path for the chrome driver
# Prefix 'r' is used to get rid of unicode errors due to path
PATH = r"C:\Users\Groot\AppData\Local\Programs\Python\Python39\Scripts\chromedriver.exe"

# Set the driver as the chromedriver.exe to control the browser
driver = webdriver.Chrome(PATH)
# As soon the browser is opened, maximize the window
driver.maximize_window()
# Navigate to the following url
driver.get("https://www.att.com/")
# Lookup element by link text
search = driver.find_element_by_id("z1-profile-text")
# Once found, click on the link
search.click()
print("clicked on Account resulting in a dropdown list")
time.sleep(5)
driver.quit()

