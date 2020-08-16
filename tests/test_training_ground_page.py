from pytest import mark
from pages.training_ground_page import TrainingGroundPage

@mark.xfail(reason="Fails on purpose.")
def test_training_page(chrome_driver):
    trng_page = TrainingGroundPage(driver=chrome_driver)
    trng_page.go()
    assert trng_page.button1.text == 'Button2', "Unexpected button1 text!"
