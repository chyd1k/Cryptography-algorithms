from PyQt5 import QtWidgets
from Hill import Hill_interface, HillCipher


class HillApp(QtWidgets.QMainWindow,
              Hill_interface.Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        self.cipher = HillCipher.Hill()

        self.btnSetKey.clicked.connect(self.setKeyWord)
        self.btnEncrypt.clicked.connect(self.encrypt)
        self.btnDecrypt.clicked.connect(self.decrypt)

    def setKeyWord(self):
        try:
            keyword = self.lineEditKey.text()
            result = self.cipher.setKeyword(keyword)
        except Exception:
            self.lineEditKey.setText("Something went wrong setting the key")
            return
        if result:
            self.lineEditKey.setText("Key set successfully")
        else:
            self.lineEditKey.setText("Something went wrong setting the key")

    def encrypt(self):
        try:
            plain_text = self.lineEditOpenText.text()
            plain_text = self.cipher.encrypt(plain_text)
        except Exception:
            return
        self.lineEditOpenText.clear()
        self.lineEditCiphertext.setText(plain_text)

    def decrypt(self):
        try:
            ciphertext = self.lineEditCiphertext.text()
            ciphertext = self.cipher.decrypt(ciphertext)
        except Exception:
            return
        self.lineEditCiphertext.clear()
        self.lineEditOpenText.setText(ciphertext)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HillApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
