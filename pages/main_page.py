from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser)

    def cross_to_catalog(self):
        coffe_link = self.browser.find_element(*MainPageLocators.coffe_link)
        coffe_link.click()
        WebDriverWait(self.browser, 20).until(EC.url_matches('https://www.torrefacto.ru/catalog/roasted/'))

    def should_open_catalog(self):
        current_url = self.browser.current_url
        assert current_url == 'https://www.torrefacto.ru/catalog/roasted/', f'Expected: https://www.torrefacto.ru/catalog/roasted/. Actual: {current_url}'