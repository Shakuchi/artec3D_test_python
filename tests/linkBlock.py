from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, TimeoutException
from contextlib import redirect_stdout


def count_page_without_link(firstPage, page_number):
    firstPage.go_to_next_page(page_number)
    try:
        firstPage.click_on_link()
    except ElementNotInteractableException:
        with open('testResult.txt', 'a') as f:
            with redirect_stdout(f):
                print(str(page_number) + " - page without visible link")
        firstPage.go_to_next_page(page_number)
    except NoSuchElementException:
        with open('testResult.txt', 'a') as f:
            with redirect_stdout(f):
                print(str(page_number) + " - page without link in page html")
        firstPage.go_to_next_page(page_number)
    except TimeoutException:
        with open('testResult.txt', 'a') as f:
            with redirect_stdout(f):
                print(str(page_number) + " - page without link in page html")
        firstPage.go_to_next_page(page_number)
