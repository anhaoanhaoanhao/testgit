'''
@File:web1.py
@DateTime:2021/12/12 14:01
@Author:hb
@Desc:
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(executable_path=r"D:\python36\driver\chromedriver.exe")
driver.maximize_window()
driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")



