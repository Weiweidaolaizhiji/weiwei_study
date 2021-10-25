#daobao
import unittest
from api.login import loginApi
import  app
from utlis import common_assert
#chuangjianceshilei
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = loginApi()
    #def tearDown(self):
    #    pass
#dingyi测试用例
    def test01_case001(self):
        #调用登录接口进行登录
        response = self.login_api.login({"mobile":"13800000002","password":"123456"})
        print(response.json())
        #assert
        #self.assertEqual(200,response.status_code)
        #self.assertEqual(True,response.json().get("success"))
        common_assert(self,response,200,True)
        # 提取token信息
        app.TOKEN = response.json().get("data")
        print(app.TOKEN)
        app.headers_data["Authorization"] = "Bearer "+ app.TOKEN
        print(app.headers_data["Authorization"])
    #case002无参数
    # 调用登录接口进行登录
    def test02_case002(self):
        response = self.login_api.login({"mobile": "", "password": "123456"})
        print(response.json())
        # assert
        #self.assertEqual(200, response.status_code)
        #self.assertEqual(True, response.json().get("success"))
        common_assert(self,response,200,True)

