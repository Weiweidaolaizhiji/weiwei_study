#导包
import requests
import app
#定义登录接口类
class EmployeeAPI:
    # 初始化
    def __init__(self):
        self.url_add_employee = app.BASE_URL+ "/api/sys/user"
        self.url_modify_employee = app.BASE_URL+ "/api/sys/user/{}"
        self.url_select_employee = app.BASE_URL+ "/api/sys/user/{}"
        self.url_delete_employee = app.BASE_URL+ "/api/sys/user/{}"

    #员工添加
    def add_employee(self,add_employee_data):
        re = requests.post(self.url_add_employee,json=add_employee_data,headers= app.headers_data)
        return re
    #员工修改
    def modify_employee(self,employee_id,update_data):
        url = self.url_modify_employee.format(employee_id)
        return requests.put(url=url,json=update_data,headers=app.headers_data)
    #员工查询
    def select_employee(self,employee_id):
        url = self.url_select_employee.format(employee_id)
        return requests.get(url=url,headers=app.headers_data)

    #员工删除
    def delete_employee(self,employee_id):
        url = self.url_delete_employee.format(employee_id)
        return requests.delete(url=url,headers=app.headers_data)