from selenium import webdriver
from PageObject.IndexPage import IndexPage
from Usecase.Login import login_final_to_index_page
from PageObject.UserPage import UserPage
from PageObject.HeadPhotoInputPage import HeadPhotoInputPage
import os
import random
import time


def get_my_new_head_path():
    all_lines = open("heads/config.txt").readlines()
    index = random.randrange(0, len(all_lines), 1, int)
    return os.path.abspath(all_lines[index])


driver = webdriver.Firefox()
page_index = IndexPage(driver, True)
login_final_to_index_page(driver, "erbadao", "erbadao")
for _ in range(10):
    page_index.get_self_user_name_link().click()
    UserPage(driver).get_fix_head_link().click()
    page_head_input = HeadPhotoInputPage(driver)
    # 决定选用哪个头像
    file_path = get_my_new_head_path()
    print(file_path)
    page_head_input.get_head_file_input().send_keys(file_path)
    page_head_input.get_submit_btn().click()
    page_index.go_to_index_page()

