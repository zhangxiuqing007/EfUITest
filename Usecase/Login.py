from selenium import webdriver
from PageObject.IndexPage import IndexPage
from PageObject.LoginInputPage import LoginInputPage
from PageObject.LoginSuccessPage import LoginSuccessPage
import time


def login_finalTo_indexPage(driver: webdriver.Chrome, account: str, pwd: str):
    index_page = IndexPage(driver, True)
    if index_page.is_login():
        print("目前处于登录状态，先注销")
        index_page.find_logOut_btn().click()
    # 打开登录页
    index_page.find_login_link().click()
    login_input_page = LoginInputPage(driver)
    # 输入账户密码登录
    login_input_page.get_account_input().send_keys(account)
    login_input_page.get_pwd_input().send_keys(pwd)
    login_input_page.get_login_btn().click()
    # 返回首页
    LoginSuccessPage(driver).get_index_link().click()


if __name__ == "__main__":
    login_finalTo_indexPage(webdriver.Chrome(), "erbadao", "erbadao")
    time.sleep(2)
