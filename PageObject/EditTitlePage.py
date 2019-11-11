from selenium import webdriver


class EditTitlePage:
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver

    def get_new_title_input(self):
        return self.driver.find_element_by_css_selector(".titleInput")

    def get_submit_btn(self):
        return self.driver.find_element_by_css_selector("input[value='提交']")

