from selenium import webdriver
from pages.trial_page import TrialPage

# Set-up
browser = webdriver.Chrome()

# Trial Page
def test_trial_page():
    trial_page = TrialPage(driver=browser)
    trial_page.go()
    trial_page.stone_input.input_text("rock")
    trial_page.stone_button.click()
    browser.quit()