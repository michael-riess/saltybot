from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import config
import web_actions


driver: WebDriver


def isLoggedIn():
    if driver.find_element(By.XPATH, '//a[@href="../authenticate?signin=1"]'):
        return False
    return True


def login():
    driver.get('https://www.saltybet.com/authenticate?signin=1')
    web_actions.enter(driver, '//input[@id="email"]', config.get('saltybet.email'))
    web_actions.enter(driver, '//input[@id="pword"]', config.get('saltybet.password'))
    web_actions.click(driver, '//span[@class="submit"]//input[@type="submit"]')


def goToMainPage():
    driver.get('https://www.saltybet.com/')


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
