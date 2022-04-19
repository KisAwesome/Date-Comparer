from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import time


FORMAT = '%b %d %Y'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 70, 401, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_2.setGeometry(QtCore.QRect(440, 70, 401, 236))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 25, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(360, 330, 161, 81))
        font = QtGui.QFont()
        # self.pushButton.setObjectName("pushButton")
        font.setPointSize(12)
        # self.pushButton.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 430, 481, 41))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 470, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 510, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 550, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 580, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 620, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 670, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(120, 320, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 350, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calculate(self, live=False):
        _d = self.calendarWidget.selectedDate().toString().split(' ')
        _d.pop(0)
        date = ' '.join(_d)
        _d2 = self.calendarWidget_2.selectedDate().toString().split(' ')
        _d2.pop(0)
        date2 = ' '.join(_d2)

        T1 = date
        T2 = date2

        if self.checkBox.isChecked() or live:
            t1 = time.time()

        else:
            t1 = time.mktime(time.strptime(T1, FORMAT))
        t2 = time.mktime(time.strptime(T2, FORMAT))

        t = t2-t1

        dd_seconds = round(t, 1)
        dd_minutes = round(t/60, 2)
        dd_hours = round(t/60/60, 2)
        dd_days = round(t/60/60/24, 1)
        dd_weeks = round(t/60/60/24/7, 2)
        dd_years = round(t/60/60/24/365, 3)
        dd_months = round(dd_years*12, 2)
        VARS = {dd_seconds: 'dd_seconds', dd_minutes: 'dd_minutes', dd_hours: 'dd_hours',
                dd_days: 'dd_days', dd_weeks: 'dd_weeks', dd_months: 'dd_months', dd_years: 'dd_years'}

        t_data = {}
        print(VARS)

        for var in VARS:
            if str(var).split('.')[1] == '0':
                t_data[VARS[var]] = int(var)
            else:
                t_data[VARS[var]] = var
        print(t_data)
        dd_seconds = t_data['dd_seconds']
        dd_minutes = t_data['dd_minutes']
        dd_hours = t_data['dd_hours']
        dd_days = t_data['dd_days']
        dd_weeks = t_data['dd_weeks']
        dd_months = t_data['dd_months']
        dd_years = t_data['dd_years']

        self.label_3.setText(f'Seconds until\t  {T2}\t{dd_seconds}')
        self.label_4.setText(f'Minutes until\t{T2}\t{dd_minutes}')
        self.label_5.setText(f'Hours until\t{T2}\t{dd_hours}')
        self.label_6.setText(f'Days until\t{T2}\t{dd_days}')
        self.label_7.setText(f'Weeks until\t{T2}\t{dd_weeks}')
        self.label_8.setText(f'Months until\t{T2}\t{dd_months}')
        self.label_9.setText(f'Years until\t{T2}\t{dd_years}')

    def CheckboxChange(self):
        if self.checkBox_2.isChecked():
            self.timer.start(1000)
            self.calendarWidget.setEnabled(False)

        else:
            self.timer.stop()
            self.calendarWidget.setEnabled(True)

    def exactTimeChange(self):
        if self.checkBox.isChecked():
            self.calendarWidget.setEnabled(False)
        else:
            self.calendarWidget.setEnabled(True)

        self.calculate()

    def update(self):
        self.calculate(live=True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "From"))
        self.label_2.setText(_translate("MainWindow", "To"))
        # self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", ""))
        # self.pushButton.clicked.connect(self.calculate)
        self.checkBox.stateChanged.connect(self.exactTimeChange)
        self.checkBox.setText(_translate("MainWindow", "Use exact time"))
        self.checkBox_2.setText(_translate("MainWindow", "Live update"))
        self.checkBox_2.stateChanged.connect(self.CheckboxChange)
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update)
        self.calendarWidget.clicked[QtCore.QDate].connect(
            lambda x: self.calculate())
        self.calendarWidget_2.clicked[QtCore.QDate].connect(
            lambda x: self.calculate())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
