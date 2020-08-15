from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(chrome_options=options)

driver = webdriver.Chrome()

username = "steeveezhouou@gmail.com"
password = "00000000@yeah"

def test_launchPage():
    driver.get('https://www.linkedin.com/')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Sign in']"))
        )
    except:
        raise RuntimeError('Unable to launch page')

def test_login():
    try:
        driver.maximize_window()
    except:
        raise RuntimeError('Unable to find window')

    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign in']"))
        )

        ActionChains(driver).click(element).perform()
    except:
        raise RuntimeError('Unable to click Sign in button')

    time.sleep(5)

    try:
        usernameBox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        passwordBox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )

        usernameBox.send_keys(username)
        passwordBox.send_keys(password)
    except:
        raise RuntimeError('Unable to input username and password')

    try:
        signInButton = WebDriverWait(driver, 200).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in']"))
        )

        driver.execute_script('arguments[0].click()', signInButton)
    except:
        raise RuntimeError('Unable to click Sign in button')

def test_logout():
    try:
        dropdownTrigger = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//artdeco-dropdown-trigger[@aria-expanded='false']"))
        )
        driver.execute_script('arguments[0].click()', dropdownTrigger)
    except:
        raise RuntimeError('Unable to find/click dropdown trigger')

    try:
        logoutHref = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Sign out']"))
        )
        driver.execute_script('arguments[0].click()', logoutHref)
    except:
        raise RuntimeError('Unable to log out')
    finally:
        driver.quit()


