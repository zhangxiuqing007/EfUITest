from selenium import webdriver


class NewPostInputPage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_title_input(self):
        return self.driver.find_element_by_css_selector(".titleInput")

    def get_content_input(self):
        return self.driver.find_element_by_css_selector(".cmtInput")

    def get_commit_btn(self):
        return self.driver.find_element_by_css_selector("input[type='submit'][value='提交']")
