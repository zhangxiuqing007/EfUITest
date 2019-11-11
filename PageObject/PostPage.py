from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class PostPage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_next_page_link(self):
        try:
            result = self.driver.find_element_by_css_selector("span+a[href*='/post']")
            return result
        except NoSuchElementException:
            return None
        except BaseException:
            return None

    def get_first_page_link(self):
        try:
            result = self.driver.find_element_by_css_selector("div a[href*='/post']")
            return result
        except NoSuchElementException:
            return None
        except BaseException:
            return None

    def get_first_user_link(self):
        element = self.driver.find_element_by_css_selector("span+a[href*='/user']")
        if element is None:
            raise BaseException()
        else:
            return element

    def get_all_pb_check_box(self):
        return self.driver.find_elements_by_css_selector("input[type='checkbox'][id*='cb']")

    def get_edit_title_link(self):
        return self.driver.find_element_by_css_selector("a[href*='/newPost?PostID=']")

    def get_fast_cmt_input(self):
        return self.driver.find_element_by_css_selector('input[name="CmtContent"]')

    def get_fast_cmt_submit(self):
        return self.driver.find_element_by_css_selector('input[type="submit"][value="提交"]')

    def get_new_cmt_btn(self):
        return self.driver.find_element_by_css_selector('a[href*="cmt?CmtID=0&CmtPageIndex="]')

    def get_cmt_edit_btn(self):
        return self.driver.find_element_by_css_selector('a[href*="/cmt?CmtID="]')
