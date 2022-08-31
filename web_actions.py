from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


def click(driver: WebDriver, query: str, queryType: str = By.XPATH):
    try:
        wait = WebDriverWait(driver, 0)
        element = wait.until(EC.element_to_be_clickable((queryType, query)))
        element.click()
    except Exception as e:
        print('Could Not Click: ', e)


def enter(driver: WebDriver, query: str, value: str, queryType: str = By.XPATH):
    try:
        wait = WebDriverWait(driver, 0)
        element = wait.until(EC.element_to_be_clickable((queryType, query)))
        element.click()
        element.send_keys(value)
    except Exception as e:
        print('Could Not Click: ', e)

