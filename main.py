import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 757)
        MainWindow.setWindowTitle("Year Percent by Shayth")
        MainWindow.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setEnabled(True)
        self.logo.setMinimumSize(QtCore.QSize(0, 479))
        self.logo.setMaximumSize(QtCore.QSize(16777215, 500))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.logo.setFont(font)
        self.logo.setStatusTip("")
        self.logo.setWhatsThis("")
        self.logo.setAccessibleName("")
        self.logo.setAccessibleDescription("")
        self.logo.setStyleSheet("color: rgb(255, 255, 255);")
        self.logo.setText("Year Percent")
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infolabel1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.infolabel1.setFont(font)
        self.infolabel1.setToolTip("")
        self.infolabel1.setStatusTip("")
        self.infolabel1.setWhatsThis("")
        self.infolabel1.setAccessibleName("")
        self.infolabel1.setAccessibleDescription("")
        self.infolabel1.setStyleSheet("color: rgb(255, 255, 255);")
        self.infolabel1.setText("Total: ")
        self.infolabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.infolabel1.setObjectName("infolabel1")
        self.horizontalLayout.addWidget(self.infolabel1)
        self.infrolabel2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.infrolabel2.setFont(font)
        self.infrolabel2.setToolTip("")
        self.infrolabel2.setStatusTip("")
        self.infrolabel2.setWhatsThis("")
        self.infrolabel2.setAccessibleName("")
        self.infrolabel2.setAccessibleDescription("")
        self.infrolabel2.setStyleSheet("color: rgb(255, 255, 255);")
        self.infrolabel2.setText("Date: ")
        self.infrolabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.infrolabel2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.infrolabel2.setObjectName("infrolabel2")
        self.horizontalLayout.addWidget(self.infrolabel2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setToolTip("")
        self.progressBar.setAccessibleName("")
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat("%p%")
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.calcbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calcbtn.setFont(font)
        self.calcbtn.setToolTip("")
        self.calcbtn.setStatusTip("")
        self.calcbtn.setWhatsThis("")
        self.calcbtn.setAccessibleName("")
        self.calcbtn.setAccessibleDescription("")
        self.calcbtn.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.calcbtn.setObjectName("calcbtn")
        self.verticalLayout.addWidget(self.calcbtn)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.calcbtn.setText("Calculate")
        self.calcbtnreact()

    # Обработка реакции кнопки - вызов функции calcperc
    def calcbtnreact(self):
        self.calcbtn.clicked.connect(self.calcperc)

    def calcperc(self):
        # Получение даты и дней
        currentdate = datetime.date.today()
        startdate = datetime.date(currentdate.year, 1, 1)
        amountofdays = datetime.date.today() - startdate
        self.infolabel1.setText("Total: " + str(amountofdays.days) + " days")
        self.infrolabel2.setText("Date: " + str(currentdate.strftime("%d-%m-%Y")))
        # Определение високосного года
        if (currentdate.year % 4 == 0 and currentdate.year % 100 != 0) or (currentdate.year % 400 == 0):
            yeardays = 366
        else:
            yeardays = 365
        # Настройка Progress Bar'а
        self.progressBar.setMaximum(yeardays - 1)
        for i in range(amountofdays.days):
            self.progressBar.setValue(i)
            time.sleep(0.005)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())