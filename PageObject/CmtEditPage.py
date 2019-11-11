from selenium import webdriver


class CmtEditPage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_cmt_input(self):
        return self.driver.find_element_by_css_selector(".cmtInput")

    def get_submit_btn(self):
        return self.driver.find_element_by_css_selector('input[type="submit"][value="提交"]')

    def get_get_images_btn(self):
        return self.driver.find_element_by_css_selector("body div button[onclick*='req']")

    def get_image_page_btns(self):
        return self.driver.find_elements_by_css_selector("div div span+button[onclick*='req']")

    def get_images_insert_btns(self):
        return self.driver.find_elements_by_css_selector("p button[onclick*='insert']")
