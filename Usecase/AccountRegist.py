from selenium import webdriver
from PageObject.IndexPage import IndexPage
from PageObject.CreateAccountInputPage import CreateAccountInputPage
from Usecase.Login import login_final_to_index_page
import uuid
import time


def create_new_account_then_login(driver: webdriver.Chrome):
    index_page = IndexPage(driver)
    index_page.logOut()  # 登出
    index_page.find_regist_btn().click()

    new_account_page = CreateAccountInputPage(driver)
    new_account_page.find_name_input().send_keys("二把刀")
    new_account_page.find_account_input().send_keys("xxxxxxxxxx")
    new_account_page.find_pwd1_input().send_keys("xxxxxxxxxx")
    new_account_page.find_pwd2_input().send_keys("xxxxxxxxxx")
    new_account_page.find_commit_btn().click()

    new_account_page.find_name_input().send_keys("三把刀")
    new_account_page.find_account_input().send_keys("erbadao")
    new_account_page.find_pwd1_input().send_keys("erbadao")
    new_account_page.find_pwd2_input().send_keys("erbadao")
    new_account_page.find_commit_btn().click()

    name = uuid.uuid4().__str__()[-8:]
    account = uuid.uuid4().__str__()
    pwd = uuid.uuid4().__str__()
    new_account_page.find_name_input().send_keys(name)
    new_account_page.find_account_input().send_keys(account)
    new_account_page.find_pwd1_input().send_keys(pwd)
    new_account_page.find_pwd2_input().send_keys(pwd)
    new_account_page.find_commit_btn().click()
    # 返回首页
    driver.get("http://127.0.0.1:8080")
    # 利用刚注册的账号 登录
    login_final_to_index_page(driver, account, pwd)


if __name__ == "__main__":
    create_new_account_then_login(webdriver.Chrome())
    time.sleep(2)
