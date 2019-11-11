from selenium import webdriver


class CreateAccountInputPage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def find_name_input(self):
        return self.driver.find_element_by_css_selector("input[name='Name']")

    def find_account_input(self):
        return self.driver.find_element_by_css_selector("input[name='Account']")

    def find_pwd1_input(self):
        return self.driver.find_element_by_css_selector("input[name='Password1']")

    def find_pwd2_input(self):
        return self.driver.find_element_by_css_selector("input[name='Password2']")

    def find_commit_btn(self):
        return self.driver.find_element_by_css_selector("input[type='submit'][value='提交']")
