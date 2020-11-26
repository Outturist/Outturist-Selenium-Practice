class BasePage:
    def __init__(self, browser, timeout=20):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    def open(self, link):
        self.browser.get(link)
