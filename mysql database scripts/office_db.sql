CREATE DATABASE btech;
USE btech;
CREATE TABLE employee (
  emp_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40),
  dob DATE,
  gender VARCHAR(1),
  address VARCHAR(100),
  ph_num VARCHAR(20),
  email_id VARCHAR (30),
  password VARCHAR(40)
);

CREATE TABLE departments (
	 dept_id VARCHAR(40) PRIMARY KEY,
     dept_name VARCHAR(50),
     dept_manager_id INT,
     FOREIGN KEY(dept_manager_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

CREATE TABLE restricted_emp(
	emp_id INT,
    dept_id VARCHAR(40),
    job_title VARCHAR(40),
    reports_to INT,
    salary INT,
    joining_date DATE,
    projects_done INT,
    projects_pending INT,
    projects_cancelled INT,
    emp_score INT,
	FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
    FOREIGN KEY(reports_to) REFERENCES employee(emp_id) ON DELETE SET NULL,
    FOREIGN KEY(dept_id) REFERENCES departments(dept_id) ON DELETE SET NULL
);

CREATE TABLE projects(
	project_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT,
    project_name VARCHAR(40),
    project_desc VARCHAR(200),
    dept_assigned VARCHAR(50),
    emps_assigned json,
    project_status VARCHAR(20)
);

CREATE TABLE client(
	client_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(40),
    address VARCHAR(100),
    projects_completed INT,
    projects_pending INT,
    projects_cancelled INT,
    email_id VARCHAR(20),
	password VARCHAR(20)
);

CREATE TABLE issues(
	issue_id INT PRIMARY KEY AUTO_INCREMENT,
	emp_id INT,
    dept_id VARCHAR(40),
    issue_desc VARCHAR(200),
    FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
    FOREIGN KEY(dept_id) REFERENCES departments(dept_id) ON DELETE SET NULL
);

CREATE TABLE notices(
	notice_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_id VARCHAR(40),
    description VARCHAR(200),
    FOREIGN KEY(dept_id) REFERENCES departments(dept_id) ON DELETE SET NULL
);

ALTER TABLE projects
ADD FOREIGN KEY(client_id)
REFERENCES client(client_id),
ADD FOREIGN KEY(dept_assigned)
REFERENCES departments(dept_id);

ALTER TABLE client 
add address VARCHAR(100); 


