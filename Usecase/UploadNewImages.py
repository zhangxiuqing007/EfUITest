from selenium import webdriver
from PageObject.IndexPage import IndexPage
from Usecase.Login import login_final_to_index_page
from PageObject.UserPage import UserPage
from PageObject.ImageUploadPage import ImageUploadPage
import os
import random
import time


def get_my_images_path():
    all_lines = open("imgs/config.txt").readlines()
    back = []
    for file in all_lines:
        back.append(os.path.abspath(file))
    return back


driver = webdriver.Firefox()
page_index = IndexPage(driver, True)
login_final_to_index_page(driver, "erbadao", "erbadao")
for _ in range(10):
    page_index.get_self_user_name_link().click()
    UserPage(driver).get_upload_img_btn().click()
    page_upload_images = ImageUploadPage(driver)
    page_upload_images.get_file_input().send_keys(get_my_images_path())
    page_upload_images.get_submit_btn().click()
    page_index.go_to_index_page()

