import mysql.connector as connector

class DatabaseConnector:
    mydb = connector.connect(
        host="localhost",
        user="root",
        password="root",
        database='python_django_lab2'
    )
    @classmethod
    def bootstrap(cls):
        cursor = cls.mydb.cursor(dictionary=True)
        cursor.execute("SELECT emp.*, dep.name department_name FROM employee emp LEFT JOIN department dep ON emp.department_id = dep.id WHERE emp.id NOT IN (SELECT emp.id FROM department dep JOIN employee emp ON dep.manager_id = emp.id)")
        employees: list[dict] = cursor.fetchall()
        cursor.execute("SELECT emp.*, dep.name department_name, dep2.name managed_department_name FROM employee emp LEFT JOIN department dep ON emp.department_id = dep.id JOIN department dep2 ON emp.id = dep2.manager_id WHERE emp.id IN (SELECT emp.id FROM department dep JOIN employee emp ON dep.manager_id = emp.id)")
        managers: list[dict] = cursor.fetchall()
        from employee import Employee
        from manager import Manager
        for e in employees:
            Employee.from_dict(e)
        for m in managers:
            Manager.from_dict(m)
            

    @classmethod
    def add_employee(cls, emp):
        department_id = cls.add_department(emp.Department)
        cursor = cls.mydb.cursor()
        cursor.execute("INSERT INTO employee (first_name, last_name, age, department_id, salary) VALUES (%s, %s, %s, %s, %s)", (emp.First_Name, emp.Last_Name, emp.Age, department_id, emp.Salary))
        cls.mydb.commit()
        return cursor.lastrowid

    @classmethod
    def transfer_employee(cls, new_dep, emp_id):
        department_id = cls.add_department(new_dep)
        cursor = cls.mydb.cursor()
        cursor.execute("UPDATE employee SET department_id = %s WHERE id = %s", (department_id, emp_id))
        cls.mydb.commit()
        return cursor.lastrowid
    
    @classmethod
    def fire_employee(cls, emp_id):
        cursor = cls.mydb.cursor()
        
        cursor.execute("DELETE FROM employee WHERE id = %s", (emp_id, ))
        cls.mydb.commit()
        
        


    @classmethod
    def get_department_by_name(cls, name):
        cursor = cls.mydb.cursor()
        cursor.execute("SELECT id FROM department WHERE name = %s", (name,))
        rows = cursor.fetchone()
        print(rows)
        return rows[0] if rows else -1

    @classmethod
    def add_department(cls, name, manager_id = None):
        department_id = cls.get_department_by_name(name)
        if department_id == -1:
            cursor = cls.mydb.cursor()
            try:
                cursor.execute("INSERT INTO department (name, manager_id) VALUES (%s, %s)", (name, manager_id))
                cls.mydb.commit()
                department_id = cursor.lastrowid
            except:
                print("Can't Add Department")
                department_id = -1
                
        elif manager_id:
            cursor = cls.mydb.cursor()
            try:
                cursor.execute("UPDATE department SET manager_id = %s WHERE id = %s", (manager_id, department_id))
                cls.mydb.commit()
            except:
                print("Can't Update Department")

        return department_id

