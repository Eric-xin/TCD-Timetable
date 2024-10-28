from src.get_cookies import get_cookies
from src.get_cookies import save_cookies
import json
import os

from selenium import webdriver
import requests

def fetch_mainpage():
    def load_cookies(file):
        with open(file, 'r') as f:
            cookies = json.load(f) 
        return cookies

    ROOT_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.join(ROOT_DIR, '..')
    CONFIG_PATH = ROOT_DIR + '/config/config.json'
    COOKIES_SAVE_PATH = ROOT_DIR + '/data/cookies.json'
    TMP_PATH = ROOT_DIR + '/tmp'

    login_credentials = json.load(open(CONFIG_PATH))

    cookies, redirect_url = get_cookies(login_credentials['username'], login_credentials['password'])

    save_cookies(cookies, COOKIES_SAVE_PATH)

    # cookies = load_cookies(dir + '/cookies.json') # load cookies from file

    driver = webdriver.Chrome()
    driver.get(redirect_url)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

    driver.save_screenshot(TMP_PATH + '/timetable.png')

# ---------------------------------------------------------------------------

# url = 'https://my.tcd.ie/urd/sits.urd/run/SIW_XTTB_1.update_timetable'
# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Accept': '*/*',
#     'Sec-Fetch-Site': 'same-origin',
#     'Accept-Language': 'en-GB,en;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Sec-Fetch-Mode': 'cors',
#     'Origin': 'https://my.tcd.ie',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15',
#     'Referer': 'https://my.tcd.ie/urd/sits.urd/run/SIW_XTTB.start_url',
#     'Content-Length': '542',
#     'Connection': 'keep-alive',
#     'Sec-Fetch-Dest': 'empty',
#     'Cookie': '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies]),
#     'Priority': 'u=3, i'
# }

# data = {
#     'P01': '20241031',
#     'P02': '03/Nov/2024',
#     'P03': '2024/25',
#     'P04': '',
#     'P05': '',
#     'P06': 'D',
#     'P07': 'TOP',
#     'P08': '',
#     'P20': '',
# }

# response = requests.post(url, headers=headers, data=data)

# print(response.text)

# with open(dir + '/timetable.html', 'w') as f:
#     f.write(response.text)

# cannot use requests to get timetable, need to use selenium