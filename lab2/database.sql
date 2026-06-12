DROP DATABASE python_django_lab2;
CREATE DATABASE IF NOT EXISTS python_django_lab2;
USE python_django_lab2;


CREATE TABLE IF NOT EXISTS department (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(15) UNIQUE,
    manager_id INT
);


CREATE TABLE IF NOT EXISTS employee (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(15),
    last_name VARCHAR(15),
    age INT,
    department_id INT,                  
    salary FLOAT,
    FOREIGN KEY (department_id) REFERENCES department(id)
);


ALTER TABLE department 
ADD FOREIGN KEY (manager_id) REFERENCES employee(id);