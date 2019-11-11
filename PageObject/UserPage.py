from selenium import webdriver


class UserPage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_user_posts_link(self):
        return self.driver.find_element_by_css_selector("a[href*='/userPost']")

    def get_fix_head_link(self):
        return self.driver.find_element_by_css_selector('a[href*="/headPhoto"]')

    def get_upload_img_btn(self):
        return self.driver.find_element_by_css_selector('input[value="上传图片"]')

