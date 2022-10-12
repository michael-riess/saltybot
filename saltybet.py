from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import config
import web_actions


driver: WebDriver

# Returns True if the system is logged into the saltybet site with a valid account
def isLoggedIn():
    if driver.find_element(By.XPATH, '//a[@href="../authenticate?signin=1"]'):
        return False
    return True


def login():
    driver.get('https://www.saltybet.com/authenticate?signin=1')
    web_actions.enter(driver, '//input[@id="email"]', config.get('saltybet.email'))
    web_actions.enter(driver, '//input[@id="pword"]', config.get('saltybet.password'))
    web_actions.click(driver, '//span[@class="submit"]//input[@type="submit"]')


# Navigates to the main page of the saltybet site
def goToMainPage():
    driver.get('https://www.saltybet.com/')


# Initializes webdriver and performs login action if necessary
def setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    goToMainPage()
    if isLoggedIn():
        pass
    else:
        login()


def teardown():
    driver.quit()
