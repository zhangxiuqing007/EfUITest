from selenium import webdriver


class LoginSuccessPage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_index_link(self):
        return self.driver.find_element_by_css_selector("a[href='/']")
