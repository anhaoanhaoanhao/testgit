'''
@File:runner.py
@DateTime:2021/12/21 23:39
@Author:hb
@Desc:
'''

import unittest
from BeautifulReport import BeautifulReport

# suite=unittest.TestSuite()
# suite.addTests(unittest.defaultTestLoader.discover(start_dir=r"D:\python36\web\testcases",pattern="test*.py"))  #测试用例所在路径
# test_runner=unittest.TextTestRunner()
# test_runner.run(suite)

#加载准备好的测试用例
cases=unittest.defaultTestLoader.discover(start_dir=r"D:\python36\web\testcases",pattern="test*.py")
#执行测试用例
result=BeautifulReport(cases)
#生成测试报告
result.report(description="系统用户的测试报告",filename="SIT测试报告",report_dir=r"D:\python36\web\report")




