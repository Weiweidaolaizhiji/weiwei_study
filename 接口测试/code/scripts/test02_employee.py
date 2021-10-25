#导包
import  unittest
from api.employee import EmployeeAPI
import requests
#创建测试类
class TestEmployee(unittest.TestCase):
    em_id = None
    def setUp(self):
        self.employee_api = EmployeeAPI()
    #添加员工
    def test01_add_employee(self):
        add_employee_data = {
                "username": "jack0709t500009",
                "mobile": "17812332179",
                "timeOfEntry": "2020-07-09",
                "formOfEmployment": 1,
                "workNumber": "10086",
                "departmentName": "销售",
                "departmentId": "1266699057968001024",
                "correctionTime": "2020-07-30T16:00:00.000Z"
            }
        reponse = self.employee_api.add_employee(add_employee_data=add_employee_data)
        print(reponse.json())
        self.assertEqual(10000,reponse.json().get("code"))
        TestEmployee.em_id = reponse.json().get("data").get("id")
        print(TestEmployee.em_id)
    #修改员工
    def test02_modify_employee(self):
        update_data = {"username":"xuwei"}
        reponse = self.employee_api.modify_employee(TestEmployee.em_id,update_data=update_data)
        print(reponse.json())
    #查询员工
    def test03_select_employee(self):
        reponse = self.employee_api.select_employee(TestEmployee.em_id)
        print(reponse.json())

    #删除员工
    def test04_delete_employee(self):
        reponse = self.employee_api.delete_employee(TestEmployee.em_id)
        print(reponse.json())