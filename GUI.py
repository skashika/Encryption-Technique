from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtWidgets import QWidget,QFormLayout,QLineEdit
import diffie_hellman
import sys

class GUI():
    def __init__(self):
        self.dh = diffie_hellman.diffieHellman()
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle('Encryptor')
        
    def build(self):
        layout = QFormLayout()
        msg_box=QLineEdit()
        layout.addRow('Message',msg_box)
        enc= QPushButton('Encrypt')
        dec=QPushButton('Decrypt')
        layout.addWidget(enc)
        layout.addWidget(dec)
        self.window.setLayout(layout)
        enc.clicked.connect(lambda: self.dh.encryption(msg_box.text()))
        dec.clicked.connect(lambda: self.dh.decrypt())
        self.window.show()
        sys.exit(self.app.exec_())


def main():
    gui = GUI()
    gui.build()

if __name__=='__main__':
    main()