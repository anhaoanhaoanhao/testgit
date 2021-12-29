'''
@File:web4.py
@DateTime:2021/12/16 23:12
@Author:hb
@Desc:
'''

import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import title_is

# def upload(filePath):
#     dialog=win32gui.FindWindow("#32770","打开")     #一级窗口
#     combox_32=win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)  #二级
#     combox=win32gui.FindWindowEx(combox_32,0,"ComboBox",None)   #三级
#     edit=win32gui.FindWindowEx(combox,0,"Edit",None)    #编辑按钮 四级
#     button=win32gui.FindWindowEx(dialog,0,"Button","打开(&0)")   #打开按钮  二级
#     #往编辑中，输入文件路径
#     win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,r"C:\Users\WIN10\Desktop\test.jpg")   #发送文件路径
#     win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)          #点击打开按钮

# 打开浏览器
s=Service(executable_path=r"D:\python36\driver\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")
driver.find_element(By.ID,"account").send_keys("shelly")
driver.find_element(By.NAME,"password").send_keys("p@ssw0rd")
driver.find_element(By.ID,"submit").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"测试").click()
driver.find_element(By.XPATH,"//nav[@id= 'subNavbar']/ul/li[1]/a").click()
driver.find_element(By.LINK_TEXT,"提Bug").click()
driver.find_element(By.CLASS_NAME,"search-field").click()
driver.find_element(By.CLASS_NAME,"active-result").click()
driver.find_element(By.ID,'title').send_keys("test")
time.sleep(2)
js="var q=document.documentElement.scrollTop=1000"
driver.execute_script(js)
time.sleep(2)
driver.find_element(By.XPATH,"//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
time.sleep(2)
dialog=win32gui.FindWindow("#32770","打开")     #一级窗口
combox_32=win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)  #二级
combox=win32gui.FindWindowEx(combox_32,0,"ComboBox",None)   #三级
edit=win32gui.FindWindowEx(combox,0,"Edit",None)    #编辑按钮 四级
button=win32gui.FindWindowEx(dialog,0,"Button","打开(&0)")   #打开按钮  二级
#往编辑中，输入文件路径
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,r"C:\Users\WIN10\Desktop\test.jpg")   #发送文件路径
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)
driver.find_element(By.ID,"submit").click()    #定位class




