'''
@File:web2.py
@DateTime:2021/12/13 0:08
@Author:hb
@Desc:
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 打开浏览器
s=Service(executable_path=r"D:\python36\driver\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")

# #输入用户名
# #driver.find_element_by_id("account").send_keys("admin")
driver.find_element(By.ID,"account").send_keys("admin")
#清除内容
time.sleep(5)
driver.find_element(By.ID,"account").clear()
#输入密码
#driver.find_element_by_name("password").send_keys("zentao78963")
driver.find_element(By.NAME,"password").send_keys("zentao78963")
#点击登录
#driver.find_element_by_id("submit").click()
driver.find_element(By.ID,"submit").click()

time.sleep(2)
try:
    assert driver.title=="地盘 - 禅道"
    print("passed")
except:
    print("failed")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s=Service(executable_path=r"D:\python36\driver\chromedriver.exe")
# driver=webdriver.Chrome(service=s)
#
# # driver.set_window_size(300,300)         #设置浏览器大小
#
# driver.maximize_window()       #最大化浏览器
# # driver.minimize_window()     #最小化浏览器
#
# driver.get("http://www.baidu.com")
# current_handle=driver.current_window_handle  #获取浏览器的属性 当前窗体句柄
#
# #运用javascript语句创建新的窗体
# js='window,open("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html");'
# driver.execute_script(js)   #执行javascript脚本
# #切换到第一个窗体
# time.sleep(3)
# handles=driver.window_handles
# driver.switch_to.window(handles[0])
# #浏览器 后退 刷新 前进
# # driver.back()
# # driver.refresh()
# # driver.back()
# time.sleep(4)
# driver.quit()