from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

# This code is implemented with selenium and is working as expected

def get_cookies(username, password, driver_path='chromedriver'):
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(executable_path=driver_path)

    try:
        # Open the login page
        driver.get('https://my.tcd.ie/urd/sits.urd/run/siw_lgn')

        # Locate the username and password fields
        username_field = driver.find_element(By.NAME, 'MUA_CODE.DUMMY.MENSYS.1')
        password_field = driver.find_element(By.NAME, 'PASSWORD.DUMMY.MENSYS.1')

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login to complete
        driver.implicitly_wait(10)

        # Retrieve the redirect URL
        redirect_url = driver.current_url
        # print(redirect_url)

        # The redirect_url is important as it is unique with each login. The generation of redirect_url is done by the server and is not predictable.

        # headers = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

        # # refresh the page until get the cookie 'EVISIONID'
        # while True:
        #     cookies = driver.get_cookies()
        #     if len(cookies) > 0:
        #         for cookie in cookies:
        #             if cookie['name'] == 'EVISIONID':
        #                 break
        #         else:
        #             driver.refresh()
        #             driver.implicitly_wait(10)
        #             continue
        #         break

        cookies = driver.get_cookies()
        return cookies, redirect_url

    finally:
        driver.quit()

def save_cookies(username, password, driver_path='chromedriver', output_file='cookies.json'):
    cookies = get_cookies(username, password, driver_path)
    cookies_json = json.dumps(cookies, indent=2)
    
    with open(output_file, 'w') as f:
        f.write(cookies_json)

def save_cookies(cookies, output_file='cookies.json'):
    cookies_json = json.dumps(cookies, indent=2)
    
    with open(output_file, 'w') as f:
        f.write(cookies_json)