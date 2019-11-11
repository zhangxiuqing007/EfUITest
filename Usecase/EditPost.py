from selenium import webdriver
from PageObject.IndexPage import IndexPage
from Usecase.Login import login_final_to_index_page
from PageObject.ThemePage import ThemePage
from PageObject.NewPostInputPage import NewPostInputPage
from PageObject.PostPage import PostPage
from PageObject.EditTitlePage import EditTitlePage
from PageObject.CmtEditPage import CmtEditPage
import datetime

driver = webdriver.Firefox()
page_index = IndexPage(driver, True)
login_final_to_index_page(driver, "erbadao", "erbadao")
page_index.find_theme_links()[0].click()
# 进入了第一个主题
page_theme = ThemePage(driver)
page_theme.get_new_post_link().click()
# 进入新帖输入页
page_new_post = NewPostInputPage(driver)

page_new_post.get_title_input().send_keys("标题：呵呵哒 测试" + datetime.datetime.now().strftime("%Y-%m-%d %A %H:%M:%S %f"))
page_new_post.get_content_input().send_keys("主贴内容：呵呵哒 测试" + datetime.datetime.now().strftime("%Y-%m-%d %A %H:%M:%S %f"))
page_new_post.get_commit_btn().click()  # 进入主题页，第一个帖子连接，就是刚发的帖子

page_theme.get_first_post_link().click()  # 进入第一个帖子页
page_post = PostPage(driver)
page_post.get_edit_title_link().click()  # 进入编辑标题页

page_edit_title = EditTitlePage(driver)
page_edit_title.get_new_title_input().send_keys("补充标题内容：" + datetime.datetime.now().strftime("%Y-%m-%d %A %H:%M:%S %f"))
page_edit_title.get_submit_btn().click()

page_post.get_fast_cmt_input().send_keys("自发自评论：楼上辣鸡 " + datetime.datetime.now().strftime("%Y-%m-%d %A %H:%M:%S %f"))
page_post.get_fast_cmt_submit().click()

for pb_box in page_post.get_all_pb_check_box():
    pb_box.click()

page_post.get_new_cmt_btn().click()

page_cmt_edit = CmtEditPage(driver)
page_cmt_edit.get_cmt_input().send_keys("楼上也是个辣鸡 " + datetime.datetime.now().strftime("%Y-%m-%d %A %H:%M:%S %f"))
page_cmt_edit.get_submit_btn().click()

# 开始修改评论
page_post.get_cmt_edit_btn().click()
page_cmt_edit.get_cmt_input().send_keys(
    "追加评论，大家都是辣鸡 " + datetime.datetime.now().strftime("%Y-%m-%d %A %H:%M:%S %f") + "\r\n我有很多图片呢：")
# 请求图片
page_cmt_edit.get_get_images_btn().click()
# 如果有足够多的页码，则随机翻一页
for btn in page_cmt_edit.get_image_page_btns():
    btn.click()
# 插入多张图片
for btn in page_cmt_edit.get_images_insert_btns():
    page_cmt_edit.get_cmt_input().send_keys("\r\n")
    btn.click()
page_cmt_edit.get_submit_btn().click()
