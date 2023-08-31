# LinkedIn Web Scraper using FastAPI and Selenium

## Overview

This project is a web scraper built using FastAPI and Selenium to scrape LinkedIn profiles based on a given keyword. The scraper logs into LinkedIn, navigates to the search page, and scrapes the names of LinkedIn profiles that match the keyword. It also handles pagination to scrape names from multiple pages.

## Requirements

- Python 3.x
- FastAPI
- Selenium
- Microsoft Edge WebDriver
- Environment variables for LinkedIn credentials

## Installation

1. **Clone the repository**
    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the project directory**
    ```bash
    cd <project_directory>
    ```

3. **Install the required packages**
    ```bash
    pip install fastapi selenium webdriver_manager
    ```

4. **Set environment variables for LinkedIn credentials**
    ```bash
    export LINKEDIN_USERNAME=your_username
    export LINKEDIN_PASSWORD=your_password
    ```

## Running the Application

1. **Start the FastAPI server**
    ```bash
    uvicorn main:app --reload
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:8000/` to check if the web scraper is running.

3. **To start scraping**, navigate to `http://127.0.0.1:8000/scrape/{keyword}`, replacing `{keyword}` with the keyword you want to search for on LinkedIn.

## Functions

- `create_driver()`: Initializes and returns a Selenium WebDriver for Microsoft Edge.
  
- `login_to_linkedin(driver)`: Logs into LinkedIn using the provided WebDriver.

- `paginate_and_scrape_users(driver)`: Handles pagination and scrapes LinkedIn profile names based on the search keyword.

## Endpoints

- `GET /`: Returns a message indicating that the web scraper is running.

- `GET /scrape/{keyword}`: Initiates the scraping process for the given keyword and returns the scraped LinkedIn profile names.
