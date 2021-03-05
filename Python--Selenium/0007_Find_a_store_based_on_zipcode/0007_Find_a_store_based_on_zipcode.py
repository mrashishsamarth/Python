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

# Lookup element by id to pull up the Menu list
search = driver.find_element_by_id("z1-pullMenu-open")

# Once found, click on the link
search.click()

# Find the "Find a store"
search = driver.find_element_by_xpath("/html/body/div[1]/attwc-globalnav-header/att-wcgn-header-bootstrap/div/att-wcgn-header-core/div/header/div/nav/div[1]/div[1]/div[2]/div[1]/attwc-globalnav-header-menu/ul/li[14]")
search.click()

# Input the zip code in the search bar
search = driver.find_element_by_id("q").send_keys("75050")

# Click on the search arrow
search = driver.find_element_by_class_name("Locator-searchbutton").click()
time.sleep(5)
# driver.quit()

