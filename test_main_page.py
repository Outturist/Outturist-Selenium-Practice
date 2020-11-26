from pages.main_page import MainPage
import time

def test_should_open_catalog(browser):
    main_page = MainPage(browser)
    main_page.open('https://www.torrefacto.ru/')
    main_page.cross_to_catalog()
    main_page.should_open_catalog()
    time.sleep(5)
