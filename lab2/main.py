from database_connector import DatabaseConnector
from employee import Employee
from manager import Manager

loop_message = """1. Insert An Employee
2. List All Employees
3. Transfer Employee
4. Fire Employee"""

insert_employee = """a. Insert A Normal Employee\nb. Insert A Manager"""

list_all = """Listing All Employees..."""

transfer_employee = """Which Employee Do You Want To Transfer and Where Do You Want To Transfer The Employee To?"""

fire_employee = """Which Employee Do You Want To Fire?"""

employee_fields = ["First Name","Last Name","Age","Department","Salary"]
manager_fields = employee_fields + ["Managed Department"]

def insertE(indent):
    print(f"{indent}{insert_employee}")
    choice = input(f"{indent+"\t"}Enter Your Choice: ").strip()
    insertd = "Failed"
    inputs = {}
    match choice:
        case 'a':
            for field in employee_fields:
                inputs[field] = input(f"{indent + "\t"}{field}: ")
            inserted = Employee(First_Name = inputs["First Name"], Last_Name = inputs["Last Name"], Age = inputs["Age"], Department = inputs["Department"], Salary = inputs["Salary"])
        case 'b':
            for field in manager_fields:
                inputs[field] = input(f"{indent + "\t"}{field}: ")
            inserted = Manager(First_Name = inputs["First Name"], Last_Name = inputs["Last Name"], Age = inputs["Age"], Department = inputs["Department"], Salary = inputs["Salary"], Managed_Department=inputs["Managed Department"])
    print(f"{indent + "\t"}{inserted}")
    
def printAE(indent):
    print(f"{indent}{list_all}")
    Employee.List_employees(indent+"\t")

def tranE(indent):
    print(f"{indent}{transfer_employee}")
    emp_list = Employee.get_employees_list()
    for emp in emp_list:
        print(f"{indent + "\t"}{emp.Id_DB} => {emp.First_Name} {emp.Last_Name}")
    choice = int(input("Enter Your Choice: ").strip())
    found_item = next((emp for emp in emp_list if emp.Id_DB == choice), None)
    if not found_item:
        print(f"{indent + "\t"}Wrong Choice!")
    else:
        found_item.transfer(input(f"{indent + "\t"}What is the Name of the New Department?: ").strip())

def fireE(indent):
    print(f"{indent}{fire_employee}")
    emp_list = Employee.get_employees_list()
    for emp in emp_list:
        print(f"{indent + "\t"}{emp.Id_DB} => {emp.First_Name} {emp.Last_Name}")
    choice = int(input("Enter Your Choice: ").strip())
    found_item = next((emp for emp in emp_list if emp.Id_DB == choice), None)
    if not found_item:
        print(f"{indent + "\t"}Wrong Choice!")
    else:
        print(f"{indent + "\t"}{found_item.fire()}")
    

# print(list_pro_max)
# # from manager import Manager

# # e1 = Employee("marwan", "asrhaf", 28, "OS", 5000)
# # e2 = Employee("marwan", "asrhaf", 28, "OS", 6000)
# # m1 = Manager("marwan", "asrhaf", 28, "OS", 6000, "OS")

# # Employee.List_employees()
# # print(e1.fire())
# # Employee.List_employees()

# # # e1.show()
# # print(DatabaseConnector.get_department_by_name("oss"))
# DatabaseConnector.bootstrap()
# Employee.List_employees()
# # print(DatabaseConnector.add_department("mac os", 1))

DatabaseConnector.bootstrap()
indent = ""
while True:
    print(loop_message)
    choice = int(input().strip())
    match choice:
        case 1:
            insertE(indent+"\t")
        case 2:
            printAE(indent+"\t")
        case 3:
            tranE(indent+"\t")
        case 4:
            fireE(indent+"\t")
    print(50 * "-")