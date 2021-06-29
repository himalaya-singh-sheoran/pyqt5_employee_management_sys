from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ast import literal_eval
import MySQLdb
import sys
from qt_material import apply_stylesheet


from PyQt5.uic import loadUiType
ui,_ = loadUiType('db_admin.ui')

class MainApp(QMainWindow,ui):
    def __init__(self,emp_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="Wonder@kid123",
            database='btech'
        )
        #style = open('material_dark.css','r')
        #style = open('elegant_dark.css','r')
        #style = open('neon_buttons.css','r')
        #style = open('manjaromix.css','r')
        #style = open('dark.css','r')
        #style = open('darkblue.css','r')
        style = open('stylenavy.css','r')
        style = style.read()
        self.setStyleSheet(style)

        self.emp_id = emp_id
        self.tabs_disappear()
        self.actionYour_Details.triggered.connect(self.your_details)
        self.actionEdit_Details.triggered.connect(self.edit_details)
        self.actionsearch_edit_employee.triggered.connect(self.search_employee_tab)
        self.actionadd_new_employee.triggered.connect(self.add_new_employee_tab)
        self.actionsearch_edit_departments.triggered.connect(self.anm_departments_tab)
        self.actionadd_new_client.triggered.connect(self.clients_tab)
        self.actionall_projects.triggered.connect(self.all_projects)
        self.actionadd_new_project_2.triggered.connect(self.search_modify_project_tab)
        self.actionadd_new_project_3.triggered.connect(self.add_new_project_tab)    
        self.actionDepartments.triggered.connect(self.departments)     
        self.actionCreate_Issue_2.triggered.connect(self.create_issue_tab)
        self.actionEdit_Issue.triggered.connect(self.edit_issue_tab)


        self.pushButton.clicked.connect(self.save_personal_changes)
        self.pushButton_7.clicked.connect(self.search_employee)   
        self.pushButton_9.clicked.connect(self.save_emp_data_changes)
        self.pushButton_10.clicked.connect(self.delete_employee)   
        self.pushButton_11.clicked.connect(self.add_employee)   
        self.pushButton_12.clicked.connect(self.search_department)   
        self.pushButton_13.clicked.connect(self.save_department)   
        self.pushButton_14.clicked.connect(self.delete_department)   
        self.pushButton_15.clicked.connect(self.add_department)   
        self.pushButton_16.clicked.connect(self.search_client)   
        self.pushButton_17.clicked.connect(self.delete_client)   
        self.pushButton_19.clicked.connect(self.add_client)   
        self.pushButton_21.clicked.connect(self.search_project_details)   
        self.pushButton_20.clicked.connect(self.edit_project_details)   
        self.pushButton_22.clicked.connect(self.delete_project)   
        self.pushButton_23.clicked.connect(self.add_new_project)   
        self.pushButton_8.clicked.connect(self.create_issue)
        self.pushButton_4.clicked.connect(self.search_issue)
        self.pushButton_2.clicked.connect(self.edit_issue)
        self.pushButton_5.clicked.connect(self.delete_issue)
        

    def tabs_disappear(self):
        self.tabWidget.tabBar().setVisible(False)

    def your_details(self):
        self.tabWidget.setCurrentIndex(0)
        cur = self.db.cursor()
        sql = "SELECT * FROM employee WHERE emp_id = {}".format(self.emp_id)
        cur.execute(sql)
        data = cur.fetchone()
        self.lineEdit.setText(str(data[0]))
        self.lineEdit_2.setText(str(data[1]))
        self.lineEdit_3.setText(str(data[2]))
        self.lineEdit_4.setText(str(data[3]))
        self.lineEdit_6.setText(str(data[4]))
        self.lineEdit_5.setText(str(data[5]))
        self.lineEdit_21.setText(str(data[6]))
        self.lineEdit_22.setText(str(data[7]))
        sql = "SELECT * FROM restricted_emp WHERE emp_id = {}".format(self.emp_id)
        cur.execute(sql)
        data = cur.fetchone()
        self.lineEdit_7.setText(str(data[2]))
        self.lineEdit_8.setText(str(data[3]))
        self.lineEdit_9.setText(str(data[4]))
        self.lineEdit_10.setText(str(data[1]))
        self.lineEdit_11.setText(str(data[5]))
        self.lineEdit_12.setText(str(data[6]))
        self.lineEdit_13.setText(str(data[7]))
        self.lineEdit_14.setText(str(data[8]))
        self.lineEdit_20.setText(str(data[9]))

    def edit_details(self):
        self.tabWidget.setCurrentIndex(1)
        cur = self.db.cursor()
        sql = "SELECT * FROM employee WHERE emp_id = {}".format(self.emp_id)
        cur.execute(sql)
        data = cur.fetchone()
        self.lineEdit_19.setText(str(data[1]))
        self.lineEdit_18.setText(str(data[2]))
        self.lineEdit_16.setText(str(data[3]))
        self.lineEdit_17.setText(str(data[4]))
        self.lineEdit_15.setText(str(data[5]))
        self.lineEdit_48.setText(str(data[6]))
        self.lineEdit_47.setText(str(data[7]))
        self.lineEdit_66.setText(str(data[8]))

    def save_personal_changes(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to save changes",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            first_name = self.lineEdit_19.text()
            last_name = self.lineEdit_18.text()
            dob = self.lineEdit_16.text()
            gender = self.lineEdit_17.text()
            phnum = self.lineEdit_48.text()
            email = self.lineEdit_47.text()
            address = self.lineEdit_15.text()
            password = self.lineEdit_66.text()
            cur = self.db.cursor()
            cur.execute('UPDATE employee SET first_name = "{}",last_name = "{}",dob = "{}",gender = "{}",address = "{}",ph_num = "{}",email_id = "{}",password = "{}" WHERE emp_id = 1'.format(str(first_name),str(last_name),str(dob),str(gender),str(address),str(phnum),str(email),str(password))) 
            self.db.commit()
            self.statusBar().showMessage("Changes Saved.")

    def search_employee_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(0)

    def search_employee(self):
        search_id = self.lineEdit_27.text()
        try:
            cur = self.db.cursor()
            sql = "SELECT * FROM employee WHERE emp_id = {}".format(search_id)
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit_31.setText(str(data[1]))
            self.lineEdit_26.setText(str(data[2]))
            self.lineEdit_30.setText(str(data[3]))
            self.lineEdit_37.setText(str(data[4]))
            self.lineEdit_24.setText(str(data[5]))
            self.lineEdit_28.setText(str(data[6]))
            self.lineEdit_33.setText(str(data[7]))
            sql = "SELECT * FROM restricted_emp WHERE emp_id = {}".format(self.emp_id)
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit_41.setText(str(data[1]))
            self.lineEdit_34.setText(str(data[2]))
            self.lineEdit_32.setText(str(data[3]))
            self.lineEdit_36.setText(str(data[4]))
            self.lineEdit_23.setText(str(data[5]))
            self.lineEdit_29.setText(str(data[6]))
            self.lineEdit_25.setText(str(data[7]))
            self.lineEdit_35.setText(str(data[8]))
            self.lineEdit_38.setText(str(data[9]))
        except:
            warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)

    def save_emp_data_changes(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to save changes",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                first_name = self.lineEdit_31.text()
                last_name = self.lineEdit_26.text()
                dob = self.lineEdit_30.text()
                gender = self.lineEdit_37.text()
                address = self.lineEdit_24.text()
                phnum = self.lineEdit_28.text()
                email  = self.lineEdit_33.text()
                cur = self.db.cursor()
                cur.execute('UPDATE employee SET first_name = "{}",last_name = "{}",dob = "{}",gender = "{}",address = "{}",ph_num = "{}",email_id = "{}" WHERE emp_id = 1'.format(str(first_name),str(last_name),str(dob),str(gender),str(address),str(phnum),str(email)))
                self.db.commit()
                dept_id = self.lineEdit_41.text()
                job_title = self.lineEdit_34.text()
                reports_to = self.lineEdit_32.text()
                salary = self.lineEdit_36.text()
                date_join = self.lineEdit_23.text()
                pdone = self.lineEdit_29.text()
                pending = self.lineEdit_25.text()
                cancelled = self.lineEdit_35.text()
                emp_score = self.lineEdit_38.text()
                cur = self.db.cursor()
                if reports_to == "None":
                    cur.execute('UPDATE restricted_emp SET dept_id = "{}",job_title = "{}",salary = "{}",joining_date = "{}",projects_done = "{}",projects_pending = "{}",projects_cancelled = "{}", emp_score = "{}" WHERE emp_id = 1'.format(str(dept_id),str(job_title),str(salary),str(date_join),str(pdone),str(pending),str(cancelled),str(emp_score))) 
                else :
                     cur.execute('UPDATE restricted_emp SET dept_id = "{}",job_title = "{}",reports_to = "{}",salary = "{}",joining_date = "{}",projects_done = "{}",projects_pending = "{}",projects_cancelled = "{}", emp_score = "{}" WHERE emp_id = 1'.format(str(dept_id),str(job_title),str(reports_to),str(salary),str(date_join),str(pdone),str(pending),str(cancelled),str(emp_score)))                    
                self.db.commit()

            except:
                warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)

    def delete_employee(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to delete employee",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                emp_id = self.lineEdit_27.text()  
                cur = self.db.cursor()
                cur.execute('Delete from employee WHERE emp_id = "{}"'.format(str(emp_id))) 
                self.db.commit()
                self.statusBar().showMessage("Changes Saved.")
            except:
                warning_message = QMessageBox.warning(self,"Unable to delete record.","Please try again.",QMessageBox.Ok)

    def add_new_employee_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(1)

    def add_employee(self):
        warning_message = QMessageBox.warning(self,"Add employee","Are you sure you want to add employee.",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                first_name = self.lineEdit_79.text()
                last_name = self.lineEdit_84.text()
                dob = self.lineEdit_80.text()
                gender = self.lineEdit_83.text()
                address = self.lineEdit_71.text()
                phnum = self.lineEdit_76.text()
                email  = self.lineEdit_81.text()
                cur = self.db.cursor()
                cur.execute('Insert into employee (first_name,last_name,dob,gender,address,ph_num,email_id) VALUES("{}","{}","{}","{}","{}","{}","{}")'.format(str(first_name),str(last_name),str(dob),str(gender),str(address),str(phnum),str(email)))
                self.db.commit()
                
                sql = "SELECT MAX(emp_id) from btech.employee;"
                cur.execute(sql)
                last_id = cur.fetchone()
                last_id = int(last_id[0])

                dept_id = self.lineEdit_42.text()
                job_title = self.lineEdit_77.text()
                reports_to = self.lineEdit_72.text()
                salary = self.lineEdit_73.text()
                date_join = self.lineEdit_82.text()
                emp_score = self.lineEdit_85.text()

                if reports_to == "None":
                    cur.execute('Insert into restricted_emp(emp_id,dept_id,job_title,salary,joining_date,projects_done,projects_pending,projects_cancelled,emp_score) VALUES("{}","{}","{}","{}","{}",0,0,0,"{}")'.format(str(last_id),str(dept_id),str(job_title),str(salary),str(date_join),str(emp_score)))
                else :
                    cur.execute('Insert into restricted_emp(emp_id,dept_id,job_title,reports_to,salary,joining_date,projects_done,projects_pending,projects_cancelled,emp_score) VALUES("{}","{}","{}"."{}","{}","{}","{}","{}")'.format(str(last_id),str(dept_id),str(job_title),str(reports_to),str(salary),str(date_join),str(0),str(0),str(0),str(emp_score)))
                self.db.commit()

            except:
                warning_message = QMessageBox.warning(self,"Failed to add employee","Please try again.",QMessageBox.Ok)

    def anm_departments_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(2)

    def search_department(self):
        dept_id = self.lineEdit_43.text()
        try:
            cur = self.db.cursor()
            sql = 'SELECT * FROM departments where dept_id = "{}"'.format(str(dept_id))
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit_44.setText(str(data[1]))
            self.lineEdit_45.setText(str(data[2]))
        except:
            warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)

    def save_department(self):
        
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to save changes",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                dept_id = self.lineEdit_43.text()
                dept_name = self.lineEdit_44.text()
                dept_mid = self.lineEdit_45.text()
                cur = self.db.cursor()
                sql = 'UPDATE departments SET dept_name = "{}",dept_manager_id = "{}" where dept_id = "{}"'.format(str(dept_name),str(dept_mid),str(dept_id))
                cur.execute(sql)
                self.db.commit()
                self.statusBar().showMessage("Changes Saved.")

            except:
                warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)

    def delete_department(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to delete department",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                dept_id = self.lineEdit_43.text()
                cur = self.db.cursor()
                cur.execute('Delete from departments WHERE dept_id = "{}"'.format(str(dept_id))) 
                self.db.commit()
                self.statusBar().showMessage("Changes Saved.")
            except:
                warning_message = QMessageBox.warning(self,"Unable to delete record.","Please try again.",QMessageBox.Ok)

    def add_department(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to add new department",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                dept_id = self.lineEdit_49.text()
                dept_name = self.lineEdit_50.text()
                dept_mid = self.lineEdit_46.text()
                cur = self.db.cursor()
                if dept_mid == "None":
                    sql = 'INSERT INTO departments(dept_id,dept_name) VALUES("{}","{}")'.format(str(dept_id),str(dept_name))
                    cur.execute(sql)
                else:
                    sql = 'INSERT INTO departments(dept_id,dept_name,dept_manager_id) VALUES("{}","{}","{}")'.format(str(dept_id),str(dept_name),str(dept_mid))
                    cur.execute(sql)
                self.db.commit()
                self.statusBar().showMessage("Changes Saved.")

            except:
                warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)

    def clients_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(3)

    def search_client(self):
        client_id = self.lineEdit_54.text()
        try:
            cur = self.db.cursor()
            sql = 'SELECT * FROM client where client_id = "{}"'.format(str(client_id))
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit_51.setText(str(data[1]))
            self.lineEdit_55.setText(str(data[2]))
            self.lineEdit_56.setText(str(data[3]))
            self.lineEdit_52.setText(str(data[4]))
            self.lineEdit_53.setText(str(data[6]))
            self.lineEdit_57.setText(str(data[7]))

        except:
            warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)

    def delete_client(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to delete department",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                client_id = self.lineEdit_54.text()
                cur = self.db.cursor()
                cur.execute('Delete from clients WHERE client_id = "{}"'.format(str(client_id))) 
                self.db.commit()
                self.statusBar().showMessage("Changes Saved.")
            except:
                warning_message = QMessageBox.warning(self,"Unable to delete record.","Please try again.",QMessageBox.Ok)

    def add_client(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to add new client",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                company_name = self.lineEdit_87.text()
                email = self.lineEdit_91.text()
                address = self.lineEdit_88.text()
                cur = self.db.cursor()
                sql = 'INSERT INTO clients(company_name,email_id,address) VALUES("{}","{}","{}")'.format(str(company_name),str(email,str(address)))
                cur.execute(sql)
                self.db.commit()
                self.statusBar().showMessage("Changes Saved.")

            except:
                warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)

    def all_projects(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(4)
        cur = self.db.cursor()
        cur.execute('SELECT * FROM projects')
        _data = cur.fetchall()
        self.tableWidget_2.setRowCount(len(_data))
        for row,x in enumerate(_data):
            for column,y in enumerate(x):
                self.tableWidget_2.setItem(row,column,QTableWidgetItem(str(y)))

    def search_modify_project_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(5)

    def search_project_details(self):
        project_id = self.lineEdit_58.text()
        try:
            cur = self.db.cursor()
            sql = "SELECT * FROM projects WHERE project_id = {}".format(project_id)
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit_94.setText(str(data[1]))
            self.lineEdit_92.setText(str(data[2]))
            self.lineEdit_96.setText(str(data[3]))
            self.lineEdit_95.setText(str(data[4]))
            self.lineEdit_93.setText(str(data[5]))
            self.lineEdit_78.setText(str(data[6]))
        
        except:
                warning_message = QMessageBox.warning(self,"Project not found.","Please try again.",QMessageBox.Ok)

    def edit_project_details(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to save changes",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            project_id = self.lineEdit_58.text()
            client_id = self.lineEdit_94.text()
            dept_assigned = self.lineEdit_95.text()
            project_name = self.lineEdit_92.text()
            project_desc = self.lineEdit_96.text()
            status = self.lineEdit_78.text()
            emps_assigned = self.lineEdit_93.text()
            cur = self.db.cursor()
            cur.execute('''UPDATE projects SET client_id = "{}",project_name = "{}",project_desc = "{}",dept_assigned = "{}",emps_assigned = '{}',project_status = "{}" WHERE project_id = "{}"'''.format(str(client_id),str(project_name),str(project_desc),str(dept_assigned),str(emps_assigned),str(status),str(project_id))) 
            self.db.commit()
            self.statusBar().showMessage("Changes Saved.")

    def delete_project(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to delete project?",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                project_id = self.lineEdit_58.text()
                cur = self.db.cursor()
                cur.execute('Delete from projects WHERE project_id = "{}"'.format(str(project_id))) 
                self.db.commit()
                self.statusBar().showMessage("Changes Saved.")
            except:
                warning_message = QMessageBox.warning(self,"Unable to delete record.","Please try again.",QMessageBox.Ok)        

    def add_new_project_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(6)

    def add_new_project(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to add new project",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            try:
                client_id = self.lineEdit_101.text()
                project_name  = self.lineEdit_99.text()
                project_desc  = self.lineEdit_97.text()
                dept_assigned = self.lineEdit_102.text()
                emps_assigned = self.lineEdit_100.text()

                cur = self.db.cursor()
                sql = '''INSERT INTO projects(client_id,project_name,project_desc,dept_assigned,emps_assigned) VALUES("{}","{}","{}","{}",'{}')'''.format(str(client_id),str(project_name),str(project_desc),str(dept_assigned),str(emps_assigned))

                cur.execute(sql)
                self.db.commit()
                self.statusBar().showMessage("Changes Saved.")

            except:
                warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)

    def departments(self):
        self.tabWidget.setCurrentIndex(3)
        cur = self.db.cursor()
        cur.execute('SELECT * FROM departments')
        data = cur.fetchall()
        self.tableWidget_7.setRowCount(len(data))
        for row,x in enumerate(data):
            for column,y in enumerate(x):
                self.tableWidget_7.setItem(row,column,QTableWidgetItem(str(y)))

    def create_issue_tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)

    def create_issue(self):
        warning_message = QMessageBox.warning(self,"Save issue","Do you want to submit issues?",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            dept_id = self.lineEdit_68.text()
            issue = self.lineEdit_67.text()
            cur = self.db.cursor()
            cur.execute('INSERT INTO issues(emp_id,dept_id,issue_desc) VALUES("{}","{}","{}")'.format(self.emp_id,dept_id,issue))
            self.db.commit()
            self.statusBar().showMessage("Issue Saved.")

    def edit_issue_tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(1)
    
    def search_issue(self):
        issue = self.lineEdit_40.text()
        try:
            cur = self.db.cursor()
            sql = 'SELECT * FROM issues WHERE issue_id = "{}"'.format(issue)    
            cur.execute(sql)
            data = cur.fetchone()
            if int(data[1]) != self.emp_id:
                warning_message = QMessageBox.warning(self,"Select your own issue.","This issue was not created by you.",QMessageBox.Ok)
            else:
                self.lineEdit_70.setText(str(data[2]))
                self.lineEdit_69.setText(str(data[3]))
        except:
                warning_message = QMessageBox.warning(self,"Issue not found.","Please try again.",QMessageBox.Ok)

    def edit_issue(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to save changes",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            issue = self.lineEdit_40.text()
            dept_id = self.lineEdit_70.text()
            issue_desc = self.lineEdit_69.text()
            
            cur = self.db.cursor()
            cur.execute('UPDATE issues SET dept_id = "{}",issue_desc = "{}" WHERE issue_id = "{}"'.format(str(dept_id),str(issue_desc),str(issue))) 
            self.db.commit()
            self.statusBar().showMessage("Changes Saved.")

    def delete_issue(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to delete issue",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            issue = self.lineEdit_40.text()  
            cur = self.db.cursor()
            cur.execute('Delete from issues WHERE issue_id = "{}"'.format(str(issue))) 
            self.db.commit()
            self.statusBar().showMessage("Changes Saved.")
       

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    apply_stylesheet(app, theme='dark_amber.xml')
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()