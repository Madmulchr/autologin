#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from selenium.webdriver.chrome.options import Options

# Replace these with your actual login credentials and the general page URL
general_page_url = 'https://club5.high5casino.com/'
username = 'jonslay@gmail.com'
password = 'Passiveproject2023#'

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")

# Create a new instance of the Chrome driver
driver = webdriver.Firefox()

# Navigate to the general page
driver.get(general_page_url)



# Wait for the loading overlay to disappear
WebDriverWait(driver, 15).until(
    EC.invisibility_of_element_located((By.CLASS_NAME, 'loading'))
    )

 # Perform additional mouse movements before interacting with the login button
action_chains = ActionChains(driver)
action_chains.move_by_offset(50, 50)  # Move to a specific offset from the current mouse position
action_chains.pause(random.uniform(1, 3))  # Pause for a random time between 1 and 3 seconds
action_chains.perform()

# Wait for the login button to be present on the page
login_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Log In']"))
)



    # Click the login button to bring up the username and password fields
login_button.click()

    # Click ANOTHER login button to bring up the username and password fields
login_button2 = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='buttonTextWhite' and text()='Log in with Username/Email']")))

login_button2.click()
    # Wait for the username field to be present on the page
username_field = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'extId'))
    )

WebDriverWait(driver, 15).until(
    EC.visibility_of(username_field) and EC.element_to_be_clickable((By.ID, 'extId'))
)
    # Enter the username
for char in username:
        username_field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between 0.1 and 0.3 seconds

time.sleep(3)
    # Wait for the password field to be present on the page
password_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'extPassword'))
    )

    # Enter the password
for char in password:
        password_field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between 0.1 and 0.3 seconds

    # Submit the login form
password_field.send_keys(Keys.RETURN)

    # Add a delay to ensure that the page has loaded after submitting the form
time.sleep(15)  # Adjust the delay time as needed

    # Perform further actions after login if needed


# In[ ]:





# In[ ]:




