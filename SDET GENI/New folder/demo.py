from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Print "Hi"
print("Hi")

# Open the Home Depot website
driver.get("https://www.homedepot.com/")
driver.maximize_window()

# Locate the search field and search for "hammer"
search = driver.find_element(By.ID, "typeahead-search-field-input1")
search.send_keys("hammer")
search.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(15)

# Locate and click on the login button
login = driver.find_element(By.XPATH, "//*[@id='header-nav-container']/div/button[4]/div/p")
login.click()

# Print the page source
page_source = driver.page_source
print(page_source)

# Wait for the page to load
time.sleep(16)

# Locate and click on the "Sign in" link
signin = driver.find_element(By.LINK_TEXT, "Sign in")
time.sleep(6)
signin.click()

# Wait for the sign-in page to load
time.sleep(17)

# Enter email
email = driver.find_element(By.ID, "username")
email.send_keys("gunderichardson@gmail.com")

# Wait for a while
time.sleep(4)

# Locate and click on the "Continue" button
continue_button = driver.find_element(By.ID, "sign-in-button")
continue_button.click()
