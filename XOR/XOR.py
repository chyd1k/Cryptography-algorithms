import sys
from PyQt5 import QtWidgets
from XOR import XOR_interface
from XOR import LFSR


class XORApp(QtWidgets.QMainWindow, XOR_interface.Ui_MainWindow):
    """This class implements application which encrypts and decrypts text with
    XOR cipher
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Object's fields
        self.inText = 0  # Here the entered text stores. It stores as integer
        self.key = 0  # Cipher key is stored as integer too
        self.length = 0  # This field stores the bit length of the inText

        # In this block I connect buttons for choosing files of text
        # and key to their methods
        # And the same I do for the key generation button
        self.textFileButton.clicked.connect(self.choose_text_file)
        self.keyFileButton.clicked.connect(self.choose_key_file)
        self.keyGenerateButton.clicked.connect(self.generate_key)

        # This block contains connection of all radioButtons to their methods

        # Here the first radioButtons' block  is being connected
        self.binaryTextRadioButton.clicked.connect(self.to_bin_inText)
        self.hexRadioButton.clicked.connect(self.to_hex_inText)
        self.symbolTextRadioButton.clicked.connect(self.to_symbols_inText)

        # The second one
        self.symbolKeyRadioButton.clicked.connect(self.to_symbols_key)
        self.hexKeyRadioButton.clicked.connect(self.to_hex_key)
        self.binKeyRadioButton.clicked.connect(self.to_bin_key)

        # And finally the third
        self.symbolOutTextRadioButton.clicked.connect(self.to_symbols_outText)
        self.binOutTextRadioButton.clicked.connect(self.to_bin_outText)
        self.hexOutTextRadioButton.clicked.connect(self.to_hex_outText)

        # At last I connect the encrypt button to the surprise-surprise... encrypt method
        self.encryptButton.clicked.connect(self.encrypt)

    # This method does the magic: it encrypts entered text and writes the result to the file and to the outTextEdit
    def encrypt(self):
        """This method does the magic: it encrypts entered text and writes the
        result to the file and to the outTextEdit
        """

        # Here I calculate the encryption result
        # Well, I just XOR inText with the key
        result = self.inText ^ self.key

        # Here I try to decode the result integer with utf-8 codec
        # and print it to the outTextEdit
        # Also I check the symbolOutTextRadioButton if it worked
        try:
            self.outTextEdit.setText(
                result.to_bytes(result.bit_length(), "little").decode()
            )
            self.symbolOutTextRadioButton.setChecked(True)
        # But if decoding is failed, which is the most probable variant I
        # just print results binary code to the
        # outTextEdit
        # And check the binOutTextRadioButton, of course
        except Exception:
            self.outTextEdit.setText(bin(result))
            self.binOutTextRadioButton.setChecked(True)

        # At last, I let the user choose the file to write the result
        file = QtWidgets.QFileDialog.getSaveFileName(
            self, "Сохранить как", filter="*.txt"
        )

        # But if the user clicked "Cancel", the file dialog will return None as
        # filename, so I don't write the result
        if file[0]:
            with open(file[0], "wb") as f:
                f.write(result.to_bytes(result.bit_length(), "little"))

    # Next big block of functions are intended to switch the view of the inText,
    # key and outText in the edits

    # First block switches inText view

    def to_bin_inText(self):
        """This function switch the view of text in inTextEdit to binary view
        """

        # Here I read the text from the edit
        text = self.inTextEdit.toPlainText()

        # If it has binary format, I just return
        if text[:2] == "0b":
            return

        # If it's hex
        if text[:2] == "0x":
            # I try to parse it to integer value and print it's binary code
            try:
                text = int(text, 16)
                self.inTextEdit.setText(bin(text))
                return

            # But if the parsing is failed, I just return
            # And I set the hexRadioButton to checked state,
            # cause even though I can't read this as hex,
            # it has hex format
            except Exception:
                self.hexRadioButton.setChecked(True)
                return
        # And if it's not the binary, and not the hex, it's probably symbols
        else:
            # So I try to encode this symbols to bytes with utf-8 codec
            # and interpret those bytes as integer with little
            # endian order.
            # After that I print those integer number's binary code
            try:
                text = int.from_bytes(text.encode(), "little")
                self.inTextEdit.setText(bin(text))
                return
            # If the codec is failed encoding this,
            # I just check the symbolTextRadioButton and return
            except Exception:
                self.symbolTextRadioButton.setChecked(True)
                return

    def to_hex_inText(self):
        """This method switches the view of text in inTextEdit to hex view
        """

        # Here we read the text from inTextdit
        text = self.inTextEdit.toPlainText()

        # If this text has binary view
        if text[:2] == "0b":
            # Try to parse it as integer and print it to inTextEdit in hex view
            try:
                text = int(text, 2)
                self.inTextEdit.setText(hex(text))
                return
            # If the parsing is failed,
            # set the binaryRadioButton checked and return
            except Exception:
                self.binaryTextRadioButton.setChecked(True)
                return

        # If this text has hex view already just return
        if text[:2] == "0x":
            return
        # If it's not binary or hex view, so it is symbols
        else:
            # So I try to encode those symbols with utf-8
            # And print it to the inTextEdit
            try:
                text = int.from_bytes(text.encode(), "little")
                self.inTextEdit.setText(hex(text))
            # If enocding has failed,
            # I just check the symbolTextRadioButton and return
            except Exception:
                self.symbolTextRadioButton.setChecked(True)

    def to_symbols_inText(self):
        """This method switches text in inTextEdit to symbolic view
        """
        # First, I read the text from inTextEdit
        text = self.inTextEdit.toPlainText()

        # If it has binary view
        if text[:2] == "0b":

            # I try to parse it to integer
            # Then convert it to bytes
            # And it the end decode it using utf-8 codec and print to inTextEdit
            try:
                text = int(text, 2)
                text = text.to_bytes(text.bit_length(), "little")
                self.inTextEdit.setText(text.decode())
                return
            # If something went wrong I check binaryTextRadioButton and return
            except Exception:
                self.binaryTextRadioButton.setChecked(True)
                return

        # If the text has hex view
        if text[:2] == "0x":

            # I try to parse it to integer, then convert it to bytes,
            # decode with utf-8 codec
            # And print to inTextEdit
            try:
                text = int(text, 16)
                text = text.to_bytes(text.bit_length(), "little")
                self.inTextEdit.setText(text.decode())
                return
            # If something went wrong I just check the hexRadioButton and return
            except Exception:
                self.hexRadioButton.setChecked(True)
                return
        # If it's not hex or binary I just return
        else:
            return

    # I do the same for other edits
    def to_symbols_key(self):
        key = self.keyEdit.toPlainText()
        if key[:2] == "0b":
            try:
                text = int(key, 2)
                text = text.to_bytes(text.bit_length(), "little")
                self.keyEdit.setText(text.decode())
                return
            except Exception:
                self.binKeyRadioButton.setChecked(True)
                return
        if key[:2] == "0x":
            try:
                key = int(key, 16)
                key = key.to_bytes(key.bit_length(), "little")
                self.keyEdit.setText(key.decode())
                return
            except Exception:
                self.hexKeyRadioButton.setChecked(True)
                return
        else:
            return

    def to_bin_key(self):
        key = self.keyEdit.toPlainText()
        if key[:2] == "0b":
            return
        if key[:2] == "0x":
            try:
                key = int(key, 16)
                self.keyEdit.setText(bin(key))
                return
            except Exception:
                self.hexKeyRadioButton.setChecked(True)
                return
        else:
            try:
                key = int.from_bytes(key.encode(), "little")
                self.keyEdit.setText(bin(key))
                return
            except Exception:
                self.symbolKeyRadioButton.setChecked(True)
                return

    def to_hex_key(self):
        key = self.keyEdit.toPlainText()
        if key[:2] == "0b":
            try:
                key = int(key, 2)
                self.keyEdit.setText(hex(key))
                return
            except Exception:
                self.binKeyRadioButton.setChecked(True)
                return
        if key[:2] == "0x":
            return
        else:
            try:
                key = int.from_bytes(key.encode(), "little")
                self.keyEdit.setText(hex(key))
                return
            except Exception:
                self.symbolKeyRadioButton.setChecked(True)
                return

    def to_symbols_outText(self):
        text = self.outTextEdit.toPlainText()
        if text[:2] == "0b":
            try:
                text = int(text, 2)
                text = text.to_bytes(text.bit_length(), "little")
                self.outTextEdit.setText(text.decode())
                return
            except Exception:
                self.binOutTextRadioButton.setChecked(True)
                return
        if text[:2] == "0x":
            try:
                text = int(text, 16)
                text = text.to_bytes(text.bit_length(), "little")
                self.outTextEdit.setText(text.decode())
                return
            except Exception:
                self.hexOutTextRadioButton.setChecked(True)
                return
        else:
            return

    def to_bin_outText(self):
        text = self.outTextEdit.toPlainText()
        if text[:2] == "0b":
            return
        if text[:2] == "0x":
            try:
                text = int(text, 16)
                self.outTextEdit.setText(bin(text))
                return
            except Exception:
                self.hexOutTextRadioButton.setChecked(True)
                return
        else:
            try:
                text = int.from_bytes(text.encode(), "little")
                self.outTextEdit.setText(bin(text))
                return
            except Exception:
                self.symbolOutTextRadioButton.setChecked(True)
                return

    def to_hex_outText(self):
        text = self.outTextEdit.toPlainText()
        if text[:2] == "0b":
            try:
                text = int(text, 2)
                self.outTextEdit.setText(hex(text))
                return
            except Exception:
                self.binOutTextRadioButton.setChecked(True)
                return
        if text[:2] == "0x":
            return
        else:
            try:
                text = int.from_bytes(text.encode(), "little")
                self.outTextEdit.setText(hex(text))
                return
            except Exception:
                self.symbolOutTextRadioButton.setChecked(True)
                return

    def choose_text_file(self):
        """This method is used to read the inText from file
        """

        # First, user chooses the file on the computer
        file = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файл", filter="*.txt"
        )
        # If user didn't press "Cancel" button
        if file[0]:
            # I open the file and read it as bytes
            with open(file[0], "rb") as f:
                # Also I convert bytes to integer and store the text as a number
                self.inText = int.from_bytes(f.read(), "little")
        # If user pressed "Cancel" button I just return
        else:
            return
        
        # After reading file and parsing text as integer
        # I count it's bit length for future uses
        self.length = self.inText.bit_length()

        # Then I try to convert inText to bytes and decode it with utf-8
        # After that I print it to inTextEdit
        # and set the symbolTextRadioButton checked
        try:
            self.inTextEdit.setText(
                self.inText.to_bytes(self.length, "little").decode()
            )
            self.symbolTextRadioButton.setChecked(True)
        # If something went wrong
        # I print the binary view of inText to inTextEdit
        # And set binaryTextRadioButton checked
        except Exception:
            self.inTextEdit.setText(bin(self.inText))
            self.binaryTextRadioButton.setChecked(True)

    def choose_key_file(self):
        """This method is being used to read the key from file
        """

        # In general this method does the same things as choose_text_file
        # Although at first it checks if the bit length of inText is not 0
        if self.inText.bit_length() == 0:
            self.keyEdit.setText("Длина входного текста должна быть больше 0")
            return
        file = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файл", filter="*.txt"
        )
        if file[0]:
            with open(file[0], "rb") as f:
                self.key = int.from_bytes(f.read(), "little")
        else:
            return
        try:
            key = self.key.to_bytes(self.key.bit_length(), "little")
            self.keyEdit.setText(key.decode())
            self.symbolKeyRadioButton.setChecked(True)
            return
        except Exception:
            self.keyEdit.setText(bin(self.key))
            self.binKeyRadioButton.setChecked(True)
            return

    # This method generates random key
    def generate_key(self):
        """This method generates random key
        """
        # First, I check if the length of inText is not 0
        # If it is I just return
        if self.inText.bit_length() == 0:
            self.keyEdit.setText("Длина входного текста должна быть больше 0")
            return

        # Else I go on
        # Here I generate random number with bit length equals inText bit length
        try:
            polynom = list(map(int, self.lineEditPolynom.text().split(' ')))
        except Exception:
            return
        init_value = int(self.lineEditInitial.text())
        shift_reg = LFSR.LFSR(polynom, init_value)
        self.key = int("".join(map(str, shift_reg.get_bits(self.length))), 2)

        # After that I try to convert it to bytes
        # and decode with utf-8 codec and print it to keyEdit
        try:
            key = self.key.to_bytes(self.key.bit_length(), "little")
            self.keyEdit.setText(key.decode())
            self.symbolKeyRadioButton.setChecked(True)
        # If something went wrong
        # I print the binary view of the generated number to keyEdit
        except Exception:
            self.keyEdit.setText(bin(self.key))
            self.binKeyRadioButton.setChecked(True)

        # Generated key is being saved to the file user chooses
        file = QtWidgets.QFileDialog.getSaveFileName(
            self, "Сохранить как", filter="*.txt"
        )
        if file[0]:
            with open(file[0], "wb") as f:
                f.write(self.key.to_bytes(self.length, "little"))
        else:
            return


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = XORApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
