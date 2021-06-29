from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ast import literal_eval
import MySQLdb
import sys
from qt_material import apply_stylesheet

from PyQt5.uic import loadUiType
ui,_ = loadUiType('manager.ui')

class MainApp(QMainWindow,ui):
    def __init__(self,emp_id=1):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="Wonder@kid123",
            database='btech'
        )

        style = open('stylenavy.css','r')
        style = style.read()
        self.setStyleSheet(style)

        self.emp_id = emp_id
        self.tabs_disappear()
        self.actionYour_Details.triggered.connect(self.your_details)
        self.actionEdit_Details.triggered.connect(self.edit_details)
        self.actionDepartments.triggered.connect(self.departments)
        self.actionCreate_Issue_2.triggered.connect(self.create_issue_tab)
        self.actionEdit_Issue.triggered.connect(self.edit_issue_tab)
        self.actionDepartments.triggered.connect(self.departments)
        self.actionYour_Projects.triggered.connect(self.your_projects)
        self.actionSearch_Project.triggered.connect(self.search_project_tab)
        self.actionSee_notices.triggered.connect(self.see_notices_tab)

        self.pushButton.clicked.connect(self.save_personal_changes)
        self.pushButton_3.clicked.connect(self.search_project_details)
        self.pushButton_8.clicked.connect(self.create_issue)
        self.pushButton_4.clicked.connect(self.search_issue)
        self.pushButton_12.clicked.connect(self.show_issues_table)
        
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
                self.pushButton_2.clicked.connect(self.edit_issue)
                self.pushButton_5.clicked.connect(self.delete_issue)
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

    def your_projects(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        cur = self.db.cursor()
        cur.execute('SELECT * FROM projects')
        data = cur.fetchall()

        _data = []
        for i in data:
            ls = list(literal_eval(i[5]))
            if "1" in ls:
                _data.append(i)

        self.tableWidget.setRowCount(len(_data))
        for row,x in enumerate(_data):
            for column,y in enumerate(x):
                self.tableWidget.setItem(row,column,QTableWidgetItem(str(y)))
        print(_data)

    def search_project_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)

    def search_project_details(self):
        project_id = self.lineEdit_39.text()
        try:
            cur = self.db.cursor()
            sql = "SELECT * FROM projects WHERE project_id = {}".format(project_id)
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit_60.setText(str(data[1]))
            self.lineEdit_62.setText(str(data[4]))
            self.lineEdit_61.setText(str(data[2]))
            self.lineEdit_63.setText(str(data[3]))
            self.lineEdit_64.setText(str(data[6]))
            self.lineEdit_65.setText(str(data[5]))
            self.pushButton_6.clicked.connect(self.edit_project_details)
        except:
                warning_message = QMessageBox.warning(self,"Project not found.","Please try again.",QMessageBox.Ok)
    
    def edit_project_details(self):
        warning_message = QMessageBox.warning(self,"Save changes","Are you sure you want to save changes",QMessageBox.Yes|QMessageBox.No)
        if warning_message == QMessageBox.Yes:
            project_id = self.lineEdit_39.text()
            client_id = self.lineEdit_60.text()
            dept_assigned = self.lineEdit_62.text()
            project_name = self.lineEdit_61.text()
            project_desc = self.lineEdit_63.text()
            status = self.lineEdit_64.text()
            emps_assigned = self.lineEdit_65.text()
            cur = self.db.cursor()
            cur.execute('''UPDATE projects SET client_id = "{}",project_name = "{}",project_desc = "{}",dept_assigned = "{}",emps_assigned = '{}',project_status = "{}" WHERE project_id = "{}"'''.format(str(client_id),str(project_name),str(project_desc),str(dept_assigned),str(emps_assigned),str(status),str(project_id))) 
            self.db.commit()
            self.statusBar().showMessage("Changes Saved.")
                
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

    def see_notices_tab(self):
        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_4.setCurrentIndex(0)

    def show_issues_table(self):
        if comboBox.currentIndex() == 0:
            cur = self.db.cursor()
            cur.execute('SELECT * FROM departments')
            data = cur.fetchall()
            self.tableWidget_7.setRowCount(len(data))
            for row,x in enumerate(data):
                for column,y in enumerate(x):
                    self.tableWidget_7.setItem(row,column,QTableWidgetItem(str(y)))

       
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    apply_stylesheet(app, theme='dark_amber.xml')
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()