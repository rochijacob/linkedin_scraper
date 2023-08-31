from fastapi import FastAPI, HTTPException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import os
import time

app = FastAPI()

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver

def create_driver():
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    return driver

def login_to_linkedin(driver):
    driver.get("https://www.linkedin.com/login")
    
    try:
        # Wait for the elements to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "session_key"))
        )
        
        username = driver.find_element(By.NAME, "session_key")
        password = driver.find_element(By.NAME, "session_password")
        
        # Use environment variables for sensitive information
        username.send_keys(os.getenv("LINKEDIN_USERNAME"))
        password.send_keys(os.getenv("LINKEDIN_PASSWORD"))
        password.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"An error occurred: {e}")


def paginate_and_scrape_users(driver):
    all_users = []  # List to store all user names

    while True:
        try:
            # Wait for the user information to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[@class='entity-result__title-text t-16']/a/span/span[@aria-hidden='true']"))
            )

            # Find all user name elements
            user_elements = driver.find_elements(By.XPATH, "//span[@class='entity-result__title-text t-16']/a/span/span[@aria-hidden='true']")

            for element in user_elements:
                username = element.text
                all_users.append(username)

            # Find and click the "Next" button to go to the next page
            # next_button = driver.find_element(By.XPATH, "//button[@aria-label='Siguiente']")
            # next_button.click()

            # Wait for the next page to load
            WebDriverWait(driver, 10).until(
                EC.staleness_of(user_elements[0])
            )

        except Exception as e:
            print(f"An error occurred or reached the end of pages: {str(e)}")
            break

    return all_users


@app.get("/")
def read_root():
    return {"message": "Web scraper is running"}

@app.get("/scrape/{keyword}")
def scrape(keyword: str):
    driver = create_driver()
    login_to_linkedin(driver)

    print("Username:", os.getenv("LINKEDIN_USERNAME"))
    print("Password:", os.getenv("LINKEDIN_PASSWORD"))

    # Navigate to the LinkedIn search results page
    driver.get(f"https://www.linkedin.com/search/results/all/?keywords={keyword}")

    all_users = paginate_and_scrape_users(driver)

    driver.quit()
    return {"message": f"Scraped data for keyword: {keyword}", "users": all_users}
