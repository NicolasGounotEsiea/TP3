from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 500)
        self.label1 = QLabel("Enter your hostname:", self)
        self.text = QLineEdit(self)
        self.text.move(70, 30)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 30)
        
     



        self.label3 = QLabel("Enter ip:", self)
        self.label3.move(0, 100)
        self.text2 = QLineEdit(self)
        self.text2.move(70, 140)
        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 140)
        

        self.label5 = QLabel("Enter api key:", self)
        self.label5.move(0, 200)
        self.text3 = QLineEdit(self)
        self.text3.move(70, 240)
        self.label6 = QLabel("Answer:", self)
        self.label6.move(10,    240)
        self.button3 = QPushButton("Send", self)
        self.button3.move(70, 300)

        self.button3.clicked.connect(self.on_click)
        self.button3.pressed.connect(self.on_click)

        self.show()

    def __create_url(self,res):
        openstreetmap_url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12"%(res["latitude"], res["longitude"])
        return openstreetmap_url

    def on_click(self):
        hostname = self.text.text()
        ip = self.text2.text()
        key = self.text3.text()

        if hostname == "" or ip == "" or key == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        
        else:
            res = self.__query(hostname, ip, key)
            if res:
                self.label2.setText("Hello")
                self.label2.adjustSize()
                self.show()
                Urls = main.__create_url(res)
                QDesktopServices.openUrl(QUrl(Urls))

        


        
    

    def __query(self, hostname, ip, key):
        url = "http://%s/ip/%s/?key=%s" %(hostname, ip, key)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()

   




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
   

