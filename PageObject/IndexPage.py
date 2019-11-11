from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class IndexPage:
    def __init__(self, driver: webdriver.Firefox, init=True):
        self.driver = driver
        if init:
            self.go_to_index_page()

    def find_login_link(self):
        return self.driver.find_element_by_css_selector("a[href*='/session']")

    def find_logOut_btn(self):
        return self.driver.find_element_by_css_selector("#logOut")

    def find_regist_btn(self):
        return self.driver.find_element_by_css_selector("a[href*='/account']")

    def find_theme_links(self):
        return self.driver.find_elements_by_css_selector("a[href*='/theme?ThemeID=']")

    def is_login(self):  # 是否处于登录状态
        try:
            return self.find_logOut_btn() is not None
        except NoSuchElementException:
            return False

    def logOut(self):
        if self.is_login():
            self.find_logOut_btn().click()

    def go_to_index_page(self):
        self.driver.get("http://127.0.0.1:8080")

    def get_self_user_name_link(self):
        return self.driver.find_element_by_css_selector("body a[href*='/user?UserID=']")
