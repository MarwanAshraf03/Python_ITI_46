from database_connector import DatabaseConnector

class Employee:
    __All_Employees: list['Employee'] = []
    def __init__(self, First_Name, Last_Name, Age, Department, Salary):
        # pass
        print("default init is starting")
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Age = Age
        self.Department = Department
        self.Salary = Salary
        self.Id_DB = DatabaseConnector.add_employee(self)
        Employee.__All_Employees.append(self)

    @classmethod
    def from_dict(cls, emp: dict):
        print("dict init is starting")
        obj = cls.__new__(cls)
        obj.First_Name = emp['first_name']
        obj.Last_Name = emp['last_name']
        obj.Age = emp['age']
        obj.Department = emp['department_name']
        obj.Salary = emp['salary']
        obj.Id_DB = emp['id']
        cls.__All_Employees.append(obj)
        return obj

    def transfer(self, new_department):
        self.Department = new_department
        DatabaseConnector.transfer_employee(new_department, self.Id_DB)

    def fire(self):
        try:
            DatabaseConnector.fire_employee(self.Id_DB)
            self_index =  Employee.__All_Employees.index(self)
            Employee.__All_Employees.pop(self_index)
        except:
            # pass
            print("Cannot Fire The Employee")
        return self

    def show(self):
        print(self)

    @staticmethod
    def List_employees(indent=''):
        for emp in Employee.__All_Employees:
            print(f"{indent}{emp}")

    @classmethod
    def get_employees_list(cls):
        return cls.__All_Employees.copy()

    def __str__(self):
        return f"Employee: {self.First_Name} {self.Last_Name} is {self.Age} years old, in department: {self.Department}, with salary of {self.Salary}$"
