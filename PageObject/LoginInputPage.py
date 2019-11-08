from selenium import webdriver


class LoginInputPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def get_account_input(self):
        return self.driver.find_element_by_css_selector("[name='Account']")

    def get_pwd_input(self):
        return self.driver.find_element_by_css_selector("[name='Password']")

    def get_login_btn(self):
        return self.driver.find_element_by_css_selector("#login")
