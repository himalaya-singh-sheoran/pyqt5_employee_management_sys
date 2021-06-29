from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ast import literal_eval
import MySQLdb
import sys
from qt_material import apply_stylesheet
import db_admin
import manager
import employee

from PyQt5.uic import loadUiType
login_ui,_ = loadUiType('emp_login.ui')

class Login(QWidget,login_ui):

    def __init__(self):
        QWidget.__init__(self)
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
        self.pushButton.clicked.connect(self.confirm_login)

    def confirm_login(self):
        emp_id = self.lineEdit.text()
        password = self.lineEdit_2.text()
        try:
            cur = self.db.cursor()
            sql = "SELECT password FROM employee WHERE emp_id = {}".format(int(emp_id))
            cur.execute(sql)
            data = cur.fetchone()
            real_passowd = str(data[0])
            sql = "SELECT job_title FROM restricted_emp WHERE emp_id = {}".format(int(emp_id))
            cur.execute(sql)
            data = cur.fetchone()
            job_title = str(data[0])
            print(job_title)
            if real_passowd == password:
                if job_title == "db_admin":
                    self.db_admin_window(emp_id)
                elif job_title == 'manager':
                    self.manager_window(emp_id)
                else :
                    self.employee_window(emp_id)

            elif data != password:
                warning_message = QMessageBox.warning(self,"Please try again.","Emp_ID and password don't match.",QMessageBox.Ok)
            else:
                warning_message = QMessageBox.warning(self,"Record not found.","Please try again.",QMessageBox.Ok)
        except:
            warning_message = QMessageBox.warning(self,"Unable to connect to database.","Please try again.",QMessageBox.Ok)

    def db_admin_window(self,emp_id):          
        self.w = db_admin.MainApp(emp_id)
        self.hide()
        self.w.show()

    def manager_window(self,emp_id):
        self.w = manager.MainApp(emp_id)
        self.hide()
        self.w.show()

    def employee_window(self,emp_id):
        self.w = employee.MainApp(emp_id)
        self.hide()
        self.w.show()

def main():
    app = QApplication(sys.argv)
    window = Login()
    apply_stylesheet(app, theme='dark_amber.xml')
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()