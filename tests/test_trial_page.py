from pytest import mark
from pages.trial_page import TrialPage

@mark.smoke
def test_trial_page(chrome_driver):
    trial_page = TrialPage(driver=chrome_driver)
    trial_page.go()
    trial_page.stone_input.input_text("rock")
    trial_page.stone_button.click()