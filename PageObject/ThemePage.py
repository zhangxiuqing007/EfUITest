from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class ThemePage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_next_page_link(self):
        try:
            result = self.driver.find_element_by_css_selector("span+a[href*='/theme']")
            return result
        except NoSuchElementException:
            return None
        except BaseException:
            return None

    def get_first_page_link(self):
        try:
            result = self.driver.find_element_by_css_selector("div a[href*='/theme']")
            return result
        except NoSuchElementException:
            return None
        except BaseException:
            return None

    def get_first_post_link(self):
        return self.driver.find_element_by_css_selector("a[href*='/post']")

    def get_new_post_link(self):
        return self.driver.find_element_by_css_selector("a[href*='/newPost?Theme']")
