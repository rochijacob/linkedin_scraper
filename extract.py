from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import os
import logging
import pickle

def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

class LinkedinBot:
    def __init__(self, delay: int = 3):
        self.delay = delay
        self.driver = createDriver()
    
    def login(self, email, password):
        # """Go to linkedin and login"""
        # go to linkedin:
        self.driver.maximize_window()
        self.driver.get('https://www.linkedin.com/login')
        time.sleep(self.delay)

        self.driver.find_element(By.ID, 'username').send_keys(email)
        self.driver.find_element(By.ID, 'password').send_keys(password)

        self.driver.find_element_by_id('password').send_keys(Keys.RETURN)
        time.sleep(self.delay)

    def save_cookie(self, path):
        with open(path, 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)

    def load_cookie(self, path):
        with open(path, 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                self.driver.add_cookie(cookie)





def getLinkedinLogin(self, driver: webdriver.Chrome) -> str:
        """Go to linkedin and login"""
        # go to linkedin:
        logging.info("Logging in")
        driver.maximize_window()
        driver.get('https://www.linkedin.com/login')
        time.sleep(self.delay)

        self.driver.find_element_by_id('username').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)

        self.driver.find_element_by_id('password').send_keys(Keys.RETURN)
        time.sleep(self.delay)

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")