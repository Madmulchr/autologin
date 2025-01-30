#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
general_page_url = 'https://www.fortunecoins.com/'
username = 'jonslay@gmail.com'
password = 'Passiveproject2023#'

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")

chrome_options.add_argument("--headless")

# Create a new instance of the Chrome driver
driver = webdriver.Firefox()

# Navigate to the general page
driver.get(general_page_url)

driver.set_window_size(1500, 500)  # Adjust the dimensions accordingly


# Wait for the "Log In" button to be clickable
login_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'loadingBtn') and contains(text(), 'Log In')]"))
    )

login_button.click()



    # Wait for the username field to be present on the page
username_field = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'emailAddress'))
    )

    # Enter the username
for char in username:
        username_field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random delay between 0.1 and 0.3 seconds

time.sleep(3)
    # Wait for the password field to be present on the page
password_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'password'))
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




