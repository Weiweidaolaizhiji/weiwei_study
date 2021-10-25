#导包
import requests
#创建接口类
class loginApi():
    #chushihua
    def __init__(self):
        self.url = "http://ihrm-test.itheima.net/api/sys/login"

    def login(self,login_data):
        return requests.post(self.url,json=login_data)

