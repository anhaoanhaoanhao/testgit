'''
@File:config.py
@DateTime:2021/12/26 11:07
@Author:hb
@Desc:
'''

import os
import sys
# print(os.getcwd())
# print(os.path.dirname(os.path.dirname(__file__)))

driver_path=f"{os.path.dirname(os.path.dirname(__file__))}\driver\chromedriver.exe"
url="http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html"
sheet="login"
file=r"D:\python36\web\data\testdata.xlsx"
log_path=r"D:\python36\web\log\log.txt"