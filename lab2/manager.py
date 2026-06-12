from database_connector import DatabaseConnector
from employee import Employee

class Manager(Employee):
    def __init__(self, First_Name, Last_Name, Age, Department, Salary, Managed_Department):
        print("manager: default init is starting")
        super().__init__(First_Name, Last_Name, Age, Department, Salary)
        self.Managed_Department = Managed_Department
        DatabaseConnector.add_department(Managed_Department, self.Id_DB)

    @classmethod
    def from_dict(cls, m: dict):
        print("manager: dict init is starting")
        obj = super().from_dict(m)
        obj.Managed_Department = m['managed_department_name']


    def __str__(self):
        # return super().__str__()
        return f"""Manager: {self.First_Name} {self.Last_Name} is {self.Age} years old, in department: {self.Department}, with salary of CONFIDENTIAL\nmanaging department: {self.Managed_Department}"""
