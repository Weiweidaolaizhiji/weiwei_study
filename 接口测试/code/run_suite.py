#导包
import unittest
import time
from scripts.test01_login import TestLogin
from scripts.test02_employee import TestEmployee
from tools.HTMLTestRunner import HTMLTestRunner
#组装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
#指定测试报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
#打开文件流
with open(report,"wb") as f:
    runner = HTMLTestRunner(f,title="测试报告")
#创建HTMLTESTRUNNER运行器
#生成测试报告
    runner.run(suite)


