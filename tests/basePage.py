from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://s3.eu-central-1.amazonaws.com/qa-web-test-task/'

    def find_element(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def go_to_next_page(self, page_number):
        return self.driver.get(self.base_url + str(page_number) + '.html')
