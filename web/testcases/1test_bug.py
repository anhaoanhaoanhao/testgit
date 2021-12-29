'''
@File:1test_bug.py
@DateTime:2021/12/23 19:14
@Author:hb
@Desc:
'''
import unittest
import unittest
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select


class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("打开浏览器")
        s = Service(executable_path=r"D:\python36\web\driver\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        cls.driver.quit()
        pass

    def setUp(self):
        print("登录禅道")
        self.driver.find_element(By.ID, "account").send_keys("shelly")
        self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        self.driver.find_element(By.ID, "submit").click()

    def tearDown(self):
        print("登出禅道")
        self.driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']/span[1]").click()
        self.driver.find_element(By.LINK_TEXT, "退出").click()


# 测试用例1
    def test_1_addbug_sccess(self):
        "成功添加Bug"
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        self.driver.find_element(By.XPATH, "//nav[@id= 'subNavbar']/ul/li[1]/a").click()
        self.driver.find_element(By.LINK_TEXT, "提Bug").click()
        self.driver.find_element(By.CLASS_NAME, "search-field").click()
        self.driver.find_element(By.CLASS_NAME, "active-result").click()
        self.driver.find_element(By.ID, 'title').send_keys("test")
        sleep(2)
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        sleep(2)
        self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
        sleep(2)
        dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
        combox_32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        combox = win32gui.FindWindowEx(combox_32, 0, "ComboBox", None)  # 三级
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)  # 编辑按钮 四级
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")  # 打开按钮  二级
        # 往编辑中，输入文件路径
        sleep(2)
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r"C:\Users\WIN10\Desktop\test.jpg")  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        self.driver.find_element(By.ID, "submit").click()  # 定位class
        sleep(2)
        try:
            self.assertEqual(self.driver.find_element(By.LINK_TEXT,"提Bug").text,"提Bug")
            print("创建Bug成功")
        except:
            print("添加Bug失败")

    def test_2_solvebug(self):
        "bug解决状态"
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        self.driver.find_element(By.XPATH, r"//nav[@id= 'subNavbar']/ul/li[1]/a").click()   #点击bug
        self.driver.find_element(By.XPATH,r"//tbody/tr[1]/td[11]/a[2]/i[1]").click()  #点击解决按钮
        self.driver.switch_to.frame("iframe-triggerModal")       #切换到不同的frame层
        sleep(2)
        self.driver.find_element(By.XPATH,r"//tbody/tr[1]/td[1]/div[1]/a[1]/span[1]").click()  #点击下拉框
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "ul.chosen-results>li:nth-child(4)").click()
        self.driver.find_element(By.XPATH, r"//tbody/tr[3]/td[2]/div[1]/div[1]/a[1]").click()
        sleep(2)
        self.driver.find_element(By.XPATH, r"//tbody/tr[3]/td[2]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        self.driver.switch_to.default_content()     #切换回原始层
        sleep(2)
        try:
            self.assertEqual(self.driver.find_element(By.LINK_TEXT,"提Bug").text,"提Bug")
            print("解决成功")
        except:
            print("失败")

    def test_3_colsebug(self):
        "bug关闭状态"
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        self.driver.find_element(By.XPATH, r"//nav[@id= 'subNavbar']/ul/li[1]/a").click()  # 点击bug
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"td.c-actions>a:nth-child(3)>i:nth-child(1)").click()  #点击关闭
        self.driver.switch_to.frame("iframe-triggerModal")  # 切换到不同的frame层
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        self.driver.switch_to.default_content()     #切换回原始层
        sleep(1)
        try:
            self.assertEqual(self.driver.find_element(By.LINK_TEXT,"提Bug").text,"提Bug")
            print("关闭成功")
        except:
            print("失败")



# if __name__=="__main__":
#     suite=unittest.TestSuite()
#     # suite.addTest(TestCases("test_addbug_sccess"))
#     suite.addTest(TestCases("test_bug_fixed"))
#     suite.addTest(TestCases("test_bug_closed"))
#     test_runner=unittest.TextTestRunner()
#     test_runner.run(suite)
if __name__=="__main__":
    #unittest.main()  #执行所有用例
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCases))
    test_runner = unittest.TextTestRunner()
    test_runner.run(suite)





