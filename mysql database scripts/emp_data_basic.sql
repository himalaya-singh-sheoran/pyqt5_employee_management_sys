-- employees data basic
USE btech;
INSERT INTO employee VALUES(1,"himalaya","sheoran",'2000-08-26','m','exist somewhere','987654321','him123@gmail.com',"billa123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("gaurav","goyal",'2001-01-02','m','exist somewhere','987654321','gau123@gmail.com',"gaurav123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("dhairya","sarin",'2001-01-02','m','exist somewhere','987654123','dha123@gmail.com',"dhairya123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("divij","gera",'2001-01-02','m','exist somewhere','9876543523','divij123@gmail.com',"divij123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("himank","kanwat",'2001-01-02','m','exist somewhere','9876543142','him1123@gmail.com',"himank123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("himesh","mahabi",'2001-01-02','m','exist somewhere','987654789','him2123@gmail.com',"himesh123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("ishaan","aggarwal",'2001-01-02','m','exist somewhere','987654123','ish123@gmail.com',"ishaan123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("jasmeet","singh",'2001-01-02','m','exist somewhere','987654432','jas123@gmail.com',"jasmeet123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("karan","bajaj",'2001-01-02','m','exist somewhere','987654741','kar123@gmail.com',"karan123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("kshitiz","goel",'2001-01-02','m','exist somewhere','987654350','ksh123@gmail.com',"mrstealurgirl123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("kuber","chaudhary",'2001-01-02','m','exist somewhere','987654012','kub123@gmail.com',"kk123");
INSERT INTO employee(first_name,dob,gender,address,ph_num,email_id,password) VALUES("Lakshay",'2001-01-02','m','exist somewhere','987654654','kak123@gmail.com','lakshay123');
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("madhavan","sharma",'2001-01-02','m','exist somewhere','987654915','mad123@gmail.com',"ms123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("mayank","mittal",'2001-01-02','m','exist somewhere','987654123','may123@gmail.com',"captain123");
INSERT INTO employee(first_name,last_name,dob,gender,address,ph_num,email_id,password) VALUES("ridhanm","jain",'2001-01-02','m','exist somewhere','987654789','rid123@gmail.com',"ridham123");

select * from employee;
