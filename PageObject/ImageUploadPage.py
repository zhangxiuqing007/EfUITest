from selenium import webdriver


class ImageUploadPage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_file_input(self):
        return self.driver.find_element_by_css_selector('input[name="images"]')

    def get_submit_btn(self):
        return self.driver.find_element_by_css_selector("input[value='提交']")
