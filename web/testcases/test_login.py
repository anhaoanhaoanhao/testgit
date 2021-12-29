'''
@File:test_login.py
@DateTime:2021/12/23 19:14
@Author:hb
@Desc:
'''

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageobjects.pagelogin import Loginpage
from config.config import driver_path,url,file,sheet
from data.read_write import ReadWrite
from log.log import logger

class TestCases(unittest.TestCase):

    def setUp(self):
        print("打开浏览器")
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get(url)
        self.page=Loginpage(self.driver)
        self.doc1=ReadWrite(file,sheet)

    def tearDown(self):
        print("关闭浏览器")
        self.driver.quit()

#测试用例1
    def test_login_success(self):
        "成功登录"
        data_list=self.doc1.read()
        self.page.type_username(data_list[0][0])
        self.page.type_password(data_list[0][1])
        self.page.click_login()
        time.sleep(2)
        try:
            assert self.driver.title == "我的地盘 - 禅道"
            print("验证登录成功测试-passed")
            logger.info("验证用户登录成功的信息")
            self.page.click_logout()
        except:
            print("验证登录成功测试-failed")

#测试用例2
    @unittest.skip("不执行")
    def test_login_wrongpassword(self):
        "密码错误"
        data_list = self.doc1.read()
        self.page.type_username(data_list[1][0])
        self.page.type_password(data_list[1][1])
        self.page.click_login()
        time.sleep(2)
        try:
            alert=self.driver.switch_to.alert
            assert "登录失败" in alert.text
            alert.accept()
            print("验证密码错误测试-passed")
        except:
            print("验证密码错误测试-failed")

#测试用例3
    @unittest.skip("不执行")
    def test_login_wrongadmin(self):
        "用户名错误"
        data_list = self.doc1.read()
        self.page.type_username(data_list[2][0])
        self.page.type_password(data_list[2][1])
        self.page.click_login()
        time.sleep(2)
        try:
            alert = self.driver.switch_to.alert
            assert "登录失败" in alert.text
            alert.accept()
            print("验证用户名错误测试-passed")
        except:
            print("验证用户名错误测试-failed")



