from selenium import webdriver
from Usecase.AccountRegist import create_new_account_then_login
from PageObject.IndexPage import IndexPage
from PageObject.ThemePage import ThemePage
from PageObject.PostPage import PostPage
from PageObject.UserPage import UserPage
import random
import time

# 这里直接是脚本，不能被复用
driver = webdriver.Firefox()
create_new_account_then_login(driver)
index_page = IndexPage(driver, False)
theme_page = ThemePage(driver)
post_page = PostPage(driver)
theme_count = len(index_page.find_theme_links())
for index in range(theme_count):
    index_page.find_theme_links()[index].click()  # 进入对应的主题
    for i in range(2):  # 后续访问3页
        next_page_link = theme_page.get_next_page_link()
        if next_page_link is not None:
            next_page_link.click()
    if theme_page.get_first_page_link() is not None:
        theme_page.get_first_page_link().click()  # 回到主题首页
    theme_page.get_first_post_link().click()  # 进入帖子页
    for i in range(2):  # 尝试访问评论页
        next_page_link = post_page.get_next_page_link()
        if next_page_link is not None:
            next_page_link.click()
    if post_page.get_first_page_link() is not None:  # 回到帖子评论的首页
        post_page.get_first_page_link().click()
    post_page.get_first_user_link().click()  # 查看用户页
    UserPage(driver).get_user_posts_link().click()
    driver.back()  # 返回用户页
    driver.back()  # 返回帖子页
    all_box = post_page.get_all_pb_check_box()
    for i in range(0, len(all_box), 5):
        all_box[i].click()
    index_page.go_to_index_page()  # 跳回到首页 开始测试下一个主题
