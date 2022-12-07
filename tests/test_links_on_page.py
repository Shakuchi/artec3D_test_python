from tests.page_helper import PageHelper
from tests.linkBlock import count_page_without_link


def test_check_link_on_page1(browser, page_number=1):
    firstPage = PageHelper(browser)
    while page_number <= 2500:
        count_page_without_link(firstPage, page_number)
        page_number = page_number + 1


def test_check_link_on_page_2(browser, page_number=2501):
    firstPage = PageHelper(browser)
    while page_number <= 5000:
        count_page_without_link(firstPage, page_number)
        page_number = page_number + 1


def test_check_link_on_page_3(browser, page_number=5001):
    firstPage = PageHelper(browser)
    while page_number <= 7500:
        count_page_without_link(firstPage, page_number)
        page_number = page_number + 1


def test_check_link_on_page_4(browser, page_number=7501):
    firstPage = PageHelper(browser)
    while page_number < 9999:
        count_page_without_link(firstPage, page_number)
        page_number = page_number + 1
