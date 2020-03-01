import sys
from PyQt5 import QtWidgets
from Feistel import Feistel_interface, feistel_net, Avalanche


class FeistelApp(QtWidgets.QMainWindow, Feistel_interface.Ui_MainWindow):
    """This class implements application that demonstrates work of Feistel
    cipher.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Object's field
        self.inText = b"\x00"  # This field stores input text
        self.key = 0  # This field stores key. Key is stored as integer
        self.outText = b"\x00"
        self.cipher = None

        # This field defines which function to use to generate round keys
        # for cipher
        self.generation_method = 1
        self.generateFunction1.setChecked(True)

        # This field defines which black box to use during
        # encryption and decryption
        self.black_box = 1
        self.blackBox1.setChecked(True)

        self.btnAvalancheEffect.setEnabled(False)

        # This block contains connecting events to methods that handle them
        self.btnSelectTextFile.clicked.connect(self.choose_text_file)
        self.btnSelectKeyFile.clicked.connect(self.choose_key_file)
        self.btnProcess.clicked.connect(self.process)
        self.btnAvalancheEffect.clicked.connect(
            lambda: Avalanche.AvalancheApp(self).show()
        )

        self.blackBox1.clicked.connect(self.click_BlackBox1)
        self.blackBox2.clicked.connect(self.click_BlackBox2)

        self.generateFunction1.clicked.connect(self.click_GenerateFunction1)
        self.generateFunction2.clicked.connect(self.click_GenerateFunction2)

        self.symbolViewText.clicked.connect(self.text_toSymbols)
        self.hexViewText.clicked.connect(self.text_toHex)

        self.symbolsViewKey.clicked.connect(self.key_toSymbols)
        self.hexViewKey.clicked.connect(self.key_toHex)

        self.symbolsViewOut.clicked.connect(self.out_toSymbols)
        self.hexViewOut.clicked.connect(self.out_toHex)

    def choose_text_file(self):
        """This function is being called when a user clicks the btnSelectTextFile
        """

        # User chooses txt file with text to be processed
        file = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файл", filter="*.txt"
        )

        # Contains of the file is being read to the inText object's
        # field as bytes
        if file[0]:
            try:
                with open(file[0], "rb") as f:
                    self.inText = f.read()
            except Exception:
                self.textEdit.setText(
                    "Something went wrong during reading the file"
                )
                return
        else:
            return

        # Next, I try to decode bytes
        try:
            self.textEdit.setText(self.inText.decode())
            self.symbolViewText.setChecked(True)

        # If something went wrong, I just print bytes to textEdit
        except Exception:
            self.textEdit.setText(hex(int.from_bytes(self.inText, "big")))
            self.hexViewText.setChecked(True)

    def choose_key_file(self):
        """This function is being called when a user clicks the btnSelectKeyFile
        """
        # User chooses txt file with key to be processed
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл", filter="*.txt"
        )

        # Contains of the file is being read to the key object's
        # field and parses as integer
        if file[0]:
            try:
                with open(file[0], "r") as f:
                    self.key = int(f.read())
            except Exception:
                try:
                    with open(file[0], "rb") as f:
                        self.key = int.from_bytes(f.read(), "big")
                except Exception:
                    self.keyEdit.setText(
                        "Something went wrong during reading the file"
                    )
        else:
            return

        # Here I try to convert integer to bytes and decode those bytes
        try:
            self.keyEdit.setText(int.to_bytes(
                (self.key.bit_length() + 7) // 8, "big").decode()
                                 )
            self.symbolsViewKey.setChecked(True)

        # If something fails I just print hex view of key ot the keyEdit
        except Exception:
            self.keyEdit.setText(hex(self.key))
            self.hexViewKey.setChecked(True)

    def process(self):
        """this function is being called when a user presses the btnProcess
        """
        # First, I create an object of Feistel network.
        self.cipher = feistel_net.Feistel(
            self.key,
            generation_method=self.generation_method
        )
        # Next, I process the text
        enc_text = self.cipher.process(
            self.inText, self.black_box, decrypt=self.checkDecrypt.isChecked()
        )
        self.outText = enc_text

        # Here I try to decode result bytes and print them to the outEdit
        try:
            self.outEdit.setText(enc_text.decode())
            self.symbolsViewOut.setChecked(True)
        # If decoding fails, I print result as integer value in hex view
        except Exception:
            self.outEdit.setText(hex(int.from_bytes(enc_text, "big")))
            self.hexViewOut.setChecked(True)

        # Also user can choose file to save the processing result
        file = QtWidgets.QFileDialog.getSaveFileName(
            self, "Сохранить как", filter="*.txt"
        )

        if file[0]:
            with open(file[0], "wb") as f:
                f.write(enc_text)
        self.btnAvalancheEffect.setEnabled(True)

    def click_BlackBox1(self):
        """This function is being called when user checks blackBox1 radioButton
        It just switches used black box. Also does click_BlackBox2"""
        self.black_box = 1

    def click_BlackBox2(self):
        self.black_box = 3

    def click_GenerateFunction1(self):
        """This function is being called when user checks genrateFunction1
        radioButton. It just switches used generation method. Also does
        click_GenerateFunction2
        """
        self.generation_method = 1

    def click_GenerateFunction2(self):
        self.generation_method = 2

    def text_toSymbols(self):
        """This function is being called when user checks symbolViewText
        radiobutton. It switches view of text in textEdit. Also do other
        _toSymbols functions, but for other edits
        """

        # First, I read the text from the edit
        text = self.textEdit.toPlainText()

        # If it has 0x prefix that means it has hex view
        # So I try to convert to integer, after that - to bytes
        # and finally decode those bytes
        if text[:2] == "0x":
            try:
                text = int(text, 16)
                self.textEdit.setText(
                    text.to_bytes(text.bit_length(), "big").decode()
                )
            # But if something fails, I just leave it alone
            except Exception:
                self.hexViewText.setChecked(True)
        # If text has not 0x prefix, so it has symbols view already
        else:
            return

    def text_toHex(self):
        """This function is being called when user checks hexViewText
        radiobutton. It switches view of text in textEdit. Also do other _toHex
        functions, but fo other edits
        """
        # First, I read the text from the edit
        text = self.textEdit.toPlainText()

        # If it has 0x prefix, so text already has hex view
        if text[:2] == "0x":
            return
        # If it has not 0x prefix, I try to encode text to bytes
        # and convert bytes to integer
        # After that I print hex view of this integer ot the edit
        else:
            try:
                text = int.from_bytes(text.encode(), "big")
                self.textEdit.setText(hex(text))
            # And if something fails, I just leave it alone
            except Exception:
                self.symbolViewText.setChecked(True)

    def key_toSymbols(self):

        key = self.keyEdit.toPlainText()
        if key[:2] == "0x":
            try:
                key = int(key, 16)
                self.keyEdit.setText(key.to_bytes(key.bit_length(), "big").decode())
            except:
                self.hexViewKey.setChecked(True)
        else:
            return

    def key_toHex(self):

        key = self.keyEdit.toPlainText()
        if key[:2] == "0x":
            return
        else:
            try:
                key = int.from_bytes(key.encode(), "big")
                self.keyEdit.setText(hex(key))
            except Exception:
                self.symbolsViewKey.setChecked(True)

    def out_toSymbols(self):

        out = self.outEdit.toPlainText()

        if out[:2] == "0x":
            try:
                out = int(out, 16)
                self.outEdit.setText(out.to_bytes(out.bit_length(), "big").decode())
            except Exception:
                self.hexViewOut.setChecked(True)
        else:
            return

    def out_toHex(self):

        out = self.outEdit.toPlainText()
        if out[:2] == "0x":
            return
        else:
            try:
                out = int.from_bytes(out.encode(), "big")
                self.outEdit.setText(hex(out))
            except Exception:
                self.symbolsViewOut.setChecked(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FeistelApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
