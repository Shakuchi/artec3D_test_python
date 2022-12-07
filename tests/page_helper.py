from tests.basePage import BasePage
from selenium.webdriver.common.by import By


class WebTaskPage:
    LOCATOR_LINK_TO_NEXT_PAGE = (By.XPATH, "/html/body/a")


class PageHelper(BasePage):
    def click_on_link(self):
        return self.find_element(WebTaskPage.LOCATOR_LINK_TO_NEXT_PAGE, time=2).click()

