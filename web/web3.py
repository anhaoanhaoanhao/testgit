'''
@File:web3.py
@DateTime:2021/12/13 22:02
@Author:hb
@Desc:
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import title_is

# 打开浏览器
s=Service(executable_path=r"D:\python36\driver\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")
driver.find_element(By.ID,"account").send_keys("shelly")
driver.find_element(By.NAME,"password").send_keys("p@ssw0rd")
driver.find_element(By.ID,"submit").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"组织").click()
driver.find_element(By.LINK_TEXT,"添加用户").click()
driver.find_element(By.ID,"account").send_keys("kkkk")
driver.find_element(By.ID,"password1").send_keys("zentao78963")
driver.find_element(By.ID,"password2").send_keys("zentao78963")
driver.find_element(By.ID,"realname").send_keys("kkkk21")
#定位下拉框内容时，首先确认该元素是不是select标签
#定位下拉框元素
select_elem=driver.find_element(By.ID,"role")

Select(select_elem).select_by_value("top")
# Select(select_elem).select_by_index(7)
#
# driver.find_element(By.ID,"verifyPassword").send_keys("zentao78963")
# js="var q=document.documentElement.scrollTop=1000"
# driver.execute_script(js)
# driver.find_element(By.ID,"submit").click()
# driver.find_element(By.LINK_TEXT,"用户").click()
# driver.find_element(By.ID,"bysearchTab").click()
# time.sleep(2)
# driver.find_element(By.ID,"value1").send_keys("kkkk")
# driver.find_element(By.ID,"submit").click()
# time.sleep(2)
# driver.find_element(By.CLASS_NAME,"icon-trash").click()
# time.sleep(2)
# #切换到不同的frame层，frame（name/id/index)
# driver.switch_to.frame("iframe-triggerModal")
# driver.find_element(By.ID,"verifyPassword").send_keys("p@ssw0rd")
# driver.find_element(By.ID,"submit").click()
# #在切换到原始层
# driver.switch_to.default_content()
# time.sleep(2)
# driver.find_element(By.ID,"submit").click()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #弹出框
# driver.find_element(By.ID,"submit").click()
# time.sleep(2)
# #调用alert模块定位弹出框
# #alert=Alert(driver)
# #浏览器切换到弹出框
# alert=driver.switch_to.alert
# #获取弹出框的文本信息
# value=alert.text
# print(value)
# #点击弹出框的确定按钮
# alert.accept()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from selenium.webdriver.common.action_chains import ActionChains
# s=Service(executable_path=r"D:\python36\driver\chromedriver.exe")
# driver=webdriver.Chrome(service=s)
# driver.maximize_window()
# #隐式等待:浏览器会在设定的时间内不断刷新页面找元素
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
# #获取目标的操作元素
# target_elem=driver.find_element(By.ID,"s-usersetting-top")
# #通过ActionChains移动鼠标到目标位置,并执行操作
# ActionChains(driver).move_to_element(target_elem).perform()


