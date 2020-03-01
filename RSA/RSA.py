from datetime import datetime
from PyQt5 import QtWidgets
from RSA import RSA_interface
import crypto_numbers
from RSA import RSAcipher
from DES import feist


class RSAApp(QtWidgets.QMainWindow,
             RSA_interface.Ui_MainWindow):
    """This class implements application for encrypting text using DES algorithm
    but key for DES is being encrypted with RSA
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Those are object's fields
        self.cipher = None
        self.p = None
        self.q = None
        self.length = None
        self.des_key = None
        self.des_inText = None
        self.des_outText = None

        self.btnChooseDESKey.setEnabled(False)
        self.btnChooseDESText.setEnabled(False)
        self.btnProcessDES.setEnabled(False)
        self.btnCreateDESKey.setEnabled(False)
        self.btnGenerateKeys.setEnabled(False)

        self.btnChooseRSA.clicked.connect(self.choose_file_RSA)
        self.btnGenerateRandomRSA.clicked.connect(self.generate_random_RSA)
        self.btnGenerateKeys.clicked.connect(self.generate_keys)
        self.btnImportKeys.clicked.connect(self.import_keys)
        self.btnCreateDESKey.clicked.connect(self.create_des_key)
        self.btnChooseDESKey.clicked.connect(self.choose_des_key)
        self.btnChooseDESText.clicked.connect(self.choose_des_text)
        self.btnProcessDES.clicked.connect(self.process_des)

    def choose_file_RSA(self):
        """This method is used for user to choose file with numbers p and q
        Those numbers can be used for generation public and private keys for RSA
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл с числами p и q", filter="*.txt"
        )

        if file[0]:
            try:
                with open(file[0], "r") as f:
                    self.p, self.q = list(map(int, f.readlines()))
                if self.p < 2 ** 128 or self.q < 2**128:
                    self.lineEditP.setText(f"p or q is below {2**128}")
                    return
            except Exception:
                self.lineEditP.setText(
                    "Something went wrong during reading the file"
                )
                return
            else:
                self.lineEditP.setText(str(self.p))
                self.lineEditQ.setText(str(self.q))
                self.btnGenerateKeys.setEnabled(True)

    def generate_random_RSA(self):
        """This method is used to generate random p and q which later can be
        used to generate public and private keys for RSA
        """
        try:
            self.length = int(self.lineEditLength.text())
        except Exception:
            return
        start = datetime.now()
        self.p = crypto_numbers.get_prime(self.length)
        self.q = crypto_numbers.get_prime(self.length)
        end = datetime.now()
        self.textBrowserTime.setText(f"Время генерации чисел: {end - start}")
        self.lineEditP.setText(str(self.p))
        self.lineEditQ.setText(str(self.q))
        self.btnGenerateKeys.setEnabled(True)

    def generate_keys(self):
        """This method is used to generate public and private keys for RSA. It
        uses p and q numbers which were read from file or generated previously.
        After keys are generated user can save them to files (public and private
        keys separately).
        """
        if not self.p or not self.q:
            return
        self.cipher = RSAcipher.RSA(self.p.bit_length())
        start = datetime.now()
        self.cipher.generate_keys(self.p, self.q, 65537)
        end = datetime.now()
        self.textBrowserTime.append(f"Время генерации ключей: {end - start}")
        public = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохранить открытый ключ", filter="*.key"
        )

        private = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохраниь закрытый ключ", filter="*.enc"
        )

        self.cipher.export_keys(public[0], private[0])

        self.textBrowserKeys.setText(
            f"PUBLIC KEY:\n{self.cipher.public_key}\n"
            f"PRIVATE KEY:\n{self.cipher.private_key}\n"
        )

        self.btnChooseDESKey.setEnabled(True)
        self.btnCreateDESKey.setEnabled(True)

    def import_keys(self):
        """This method is used to import keys for RSA cipher from files. These
        keys are used later to decrypt or encrypt key for DES algorithm
        """
        if not self.length:
            try:
                self.length = int(self.lineEditLength.text())
            except Exception:
                return
        self.cipher = RSAcipher.RSA(self.length)

        public = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл открытого ключа", filter="*.key"
        )

        private = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл закрытого ключа", filter="*.enc"
        )

        if public[0] and private[0]:
            self.cipher.import_keys(public[0], private[0])
            self.textBrowserKeys.setText(
                f"PUBLIC KEY:\ne = {self.cipher.public_key[0]}\n"
                f"n = {self.cipher.public_key[1]}\n"
                f"PRIVATE KEY:\nd = {self.cipher.private_key[0]}\n"
                f"n = {self.cipher.private_key[1]}\n"
            )
            self.btnChooseDESKey.setEnabled(True)
            self.btnCreateDESKey.setEnabled(True)

    def create_des_key(self):
        """This method is used to create key for DES algorithm randomly. After
        key was generated user can save it to the file and use it later to
        encrypt and decrypt files with DES algorithm.
        DES key is being encrypted with RSA algorithm using it's public key
        before writing to file.
        """
        key = crypto_numbers.get_prime(48)
        self.lineEditCreatedDESKey.setText(str(key))
        self.lineEditDesKey.setText(str(key))
        self.des_key = key
        start = datetime.now()
        key = self.cipher.encrypt(key)
        end = datetime.now()
        self.textBrowserTime.append(f"Время шифрования DES ключа: {end - start}")
        file = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохранить как", filter="*.dk"
        )

        if file[0]:
            with open(file[0], "wb") as f:
                f.write(str(key).encode())
        self.btnChooseDESText.setEnabled(True)

    def choose_des_key(self):
        """This method is used to import DES key from file. It's supposed that
        DES key is encrypted with RSA cipher. So function will try to decrypt it.
        Therefore before using this method user have to import keys for RSA.
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл с ключом", filter="*.dk"
        )

        if file[0]:
            with open(file[0], "rb") as f:
                key = int(f.read().decode())
            key = self.cipher.decrypt(key)
            self.des_key = key
            self.lineEditDesKey.setText(str(key))
            self.btnChooseDESText.setEnabled(True)

    def choose_des_text(self):
        """This method is used to read file to be encrypted/decrypted with DES
        algorithm.
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл", filter="*.txt"
        )

        if file[0]:
            with open(file[0], "r") as f:
                text = f.read()
        else:
            return
        self.des_inText = text
        self.textBrowserDesText.setText(f"{self.des_inText}")
        self.btnProcessDES.setEnabled(True)

    def process_des(self):
        """This method actually performs encryption or decryption of text
        from file.
        """
        if self.checkBoxDecrypt.isChecked():
            self.des_outText = feist.decode(self.des_inText,
                                            16, self.des_key)[1]
            self.textBrowserDesResult.setText(f"{self.des_outText}")
        else:
            self.des_outText = feist.encode(self.des_inText, 16,
                                            self.des_key)[1]
            self.textBrowserDesResult.setText(f"{self.des_outText}")

        file = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохрнить как", filter="*.txt"
        )

        if file[0]:
            with open(file[0], "w") as f:
                f.write(str(self.des_outText))
