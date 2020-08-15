import pytest
from selenium import webdriver
from pages.training_ground_page import TrainingGroundPage
from pages.trial_page import TrialPage


# Set up
browser = webdriver.Chrome()

# Training Page
@pytest.mark.xfail(reason="Fails on purpose.")
def test_training_page():
    trng_page = TrainingGroundPage(driver=browser)
    trng_page.go()
    assert trng_page.button1.text == 'Button2', "Unexpected button1 text!"

# Trial Page
@pytest.mark.smoke
def test_trial_page():
    trial_page = TrialPage(driver=browser)
    trial_page.go()
    trial_page.stone_input.input_text("rock")
    trial_page.stone_button.click()

# Clean up
@pytest.mark.cleanup
def test_quit():
    browser.quit()