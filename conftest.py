import pytest
import os
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": os.path.expanduser("~/Downloads")}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()