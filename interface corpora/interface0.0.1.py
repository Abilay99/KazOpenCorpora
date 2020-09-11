from PyQt5 import QtWidgets, QtCore, QtGui
from interfaceForm import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.clickbtn)
    def clickbtn(self):
        self.ui.pushButton.setVisible(False)
        self.ui.progressBar.setVisible(True)
        self.create_table()
        self.ui.tableWidget.setVisible(True)
    def create_table(self):
        _translate = QtCore.QCoreApplication.translate
        letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper()
        letters = letters.split(' ')
        for i in range(26):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(i, item)
            itemt = self.ui.tableWidget.horizontalHeaderItem(i)
            itemt.setText(_translate("MainWindow", letters[i]))
        for i in range(100):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(i, item)
            itemt = self.ui.tableWidget.verticalHeaderItem(i)
            itemt.setText(_translate("MainWindow", str(i+1)))
        self.ui.tableWidget.setSpan(0,0,1,2)
        self.ui.tableWidget.setSpan(0,2,1,2)
        self.ui.tableWidget.setSpan(0,4,1,2)
        row = 0
        col = 0
        mas = ["TF","IDF","TF-IDF"]
        i = 0
        while col < 5:
            item = QtWidgets.QTableWidgetItem()
            item.setText(mas[i])
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setBackground(QtGui.QColor(0, 255, 0))
            self.ui.tableWidget.setItem(row, col, item)
            col += 2
            i += 1   
        #204, 255, 255 for lines result
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
