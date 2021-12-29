'''
@File:web5.py
@DateTime:2021/12/19 23:41
@Author:hb
@Desc:
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import win32gui
import win32con
#
# s=Service(executable_path=r"D:\python36\driver\chromedriver.exe")
# driver=webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")
# driver.find_element(By.CSS_SELECTOR,"#account").send_keys("shelly")   #用CSS_SELECTOR
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys("p@ssw0rd")   #相对路径
# driver.find_element(By.CSS_SELECTOR,".form-actions :nth-child(1)").click()

# test Fixture:搭建测试的环境
import unittest

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")

    def setUp(self):
        print("登录禅道")

    def tearDown(self):
        print("登出禅道")
#测试用例1
    def test_adduser(self):
        print("执行添加组织用户测试用例")
#测试用例2
    def test_showuser(self):
        print("执行查看组织用户测试用例")
#测试用例3
    def test_updateuser(self):
        print("执行修改组织用户测试用例")
#测试用例4
    def test_deleteuser(self):
        print("执行删除组织用户测试用例")
    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")

if __name__=="__main__":
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(TestCases("test_adduser"))
    suite.addTest(TestCases("test_showuser"))
    suite.addTest(TestCases("test_updateuser"))
    suite.addTest(TestCases("test_deleteuser"))
    test_runner=unittest.TextTestRunner()
    test_runner.run(suite)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import unittest
#
# class TestCases(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         "打开浏览器"
#         s = Service(executable_path=r"D:\python36\driver\chromedriver.exe")
#         cls.driver=webdriver.Chrome(service=s)
#         cls.driver.maximize_window()
#         cls.driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")
#     @classmethod
#     def tearDownClass(cls):
#         "关闭浏览器"
#         time.sleep(10)
#         cls.driver.quit()
#     def setUp(self):
#         "登录禅道"
#         self.driver.find_element(By.ID, "account").send_keys("shelly")
#         self.driver.find_element(By.NAME,"password").send_keys("p@ssw0rd")
#         self.driver.find_element(By.ID,"submit").click()
#
#     def tearDown(self):
#         "登出禅道"
#         self.driver.find_element(By.XPATH,"//a[@class='dropdown-toggle']/span[1]").click()
#         self.driver.find_element(By.LINK_TEXT,"退出").click()
# #测试用例1
#     def test_addbug(self):
#         "执行添加组织用户测试用例"
#         time.sleep(3)
#         self.driver.find_element(By.LINK_TEXT, "测试").click()
#         self.driver.find_element(By.XPATH, "//nav[@id= 'subNavbar']/ul/li[1]/a").click()
#         self.driver.find_element(By.LINK_TEXT, "提Bug").click()
#         self.driver.find_element(By.CLASS_NAME, "search-field").click()
#         self.driver.find_element(By.CLASS_NAME, "active-result").click()
#         self.driver.find_element(By.ID, 'title').send_keys("test")
#         time.sleep(2)
#         js = "var q=document.documentElement.scrollTop=1000"
#         self.driver.execute_script(js)
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
#         time.sleep(2)
#         dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
#         combox_32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
#         combox = win32gui.FindWindowEx(combox_32, 0, "ComboBox", None)  # 三级
#         edit = win32gui.FindWindowEx(combox, 0, "Edit", None)  # 编辑按钮 四级
#         button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")  # 打开按钮  二级
#         # 往编辑中，输入文件路径
#         win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r"C:\Users\WIN10\Desktop\test.jpg")  # 发送文件路径
#         win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
#         self.driver.find_element(By.ID, "submit").click()  # 定位class
#
#
# if __name__=="__main__":
#     #unittest.main()
#     suite=unittest.TestSuite()
#     suite.addTest(TestCases("test_addbug"))
#     test_runner=unittest.TextTestRunner()
#     test_runner.run(suite)