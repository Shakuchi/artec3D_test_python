import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    yield driver
    driver.quit()
