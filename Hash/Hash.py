import random
from hashlib import sha512
from PyQt5 import QtWidgets
import crypto_numbers
from Hash import Hash_interface
from RSA import RSAcipher


class HashApp(QtWidgets.QMainWindow,
              Hash_interface.Ui_MainWindow):
    """This class implements application for signing files using
    RSA algorithm and ElGamal algorithm
    """

    def __init__(self, parent):

        super().__init__(parent)
        self.setupUi(self)

        self.q = 0
        self.p = 0
        self.public_elgamal = {"y": 0, "g": 0, "p": 0}
        self.private_elgamal = 0
        self.cipher = None
        self.signRSA = 0
        self.signElGamal = ()

        self.btnGenerateRandomRSA.clicked.connect(self.generate_random_rsa)
        self.btnChooseFileRSA.clicked.connect(self.choose_file_rsa)
        self.btnGenerateKeysRSA.clicked.connect(self.generate_keys_rsa)
        self.btnImportKeysRSA.clicked.connect(self.import_keys_rsa)
        self.btnSaveSignRSA.clicked.connect(self.save_sign_rsa)
        self.btnSignFileRSA.clicked.connect(self.sign_file_rsa)
        self.btnCheckSignRSA.clicked.connect(self.check_sign_rsa)
        self.btnGenerateRandomElGamal.clicked.connect(self.generate_random_elgamal)
        self.btnChoosePFileElGamal.clicked.connect(self.choose_pfile_elgamal)
        self.btnChooseGFileElGamal.clicked.connect(self.choose_gfile_elgamal)
        self.btnGenerateKeysElGamal.clicked.connect(self.generate_keys_elgamal)
        self.btnImportKeysElGamal.clicked.connect(self.import_keys_elgamal)
        self.btnSignFileElGamal.clicked.connect(self.sign_file_elgamal)
        self.btnSaveSignElGamal.clicked.connect(self.save_sign_elgamal)
        self.btnCheckSignElGamal.clicked.connect(self.check_sign_elgamal)

    def generate_random_rsa(self):
        """This method generates numbers p and q for RSA algorithm
        """
        self.p = crypto_numbers.get_prime(512)
        self.q = crypto_numbers.get_prime(512)
        self.lineEditP.setText(f"{self.p}")
        self.lineEditQ.setText(f"{self.q}")
        self.btnGenerateKeysRSA.setEnabled(True)

    def choose_file_rsa(self):
        """This method allows user to choose file with numbers p and q for
        RSA algorithm
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл с числами p и q", filter="*.txt"
        )

        if file[0]:
            try:
                with open(file[0], "r") as f:
                    self.p, self.q = list(map(int, f.readlines()))
                if self.p < 2 ** 128 or self.q < 2 ** 128:
                    self.lineEditP.setText(f"p or q is below {2**128}")
                    return
            except Exception:
                self.lineEditP.setText(
                    "Somethong went wrong during reading the file"
                )
            else:
                self.lineEditP.setText(f"{self.p}")
                self.lineEditQ.setText(f"{self.q}")
            self.btnGenerateKeysRSA.setEnabled(True)

    def generate_keys_rsa(self):
        """This method generates public and private keys for signing files with
        RSA algorithm.
        """
        if not self.p and not self.q:
            return
        self.cipher = RSAcipher.RSA(self.p.bit_length())
        self.cipher.generate_keys(self.p, self.q, 65537)
        private = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохранить закрытый ключ", filter="*.privrsa"
        )[0]

        public = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохраниь открытый ключ", filter="*.pubrsa"
        )[0]
        if private and public:
            self.cipher.export_keys(public, private)
            self.cipher.private_key, self.cipher.public_key = self.cipher.public_key, self.cipher.private_key

        self.textBrowserKeysRSA.setText(
            f"PUBLIC KEY:\n{self.cipher.private_key}\n"
            f"PRIVATE KEY:\n{self.cipher.public_key}\n"
        )
        self.btnSignFileRSA.setEnabled(True)
        self.btnCheckSignRSA.setEnabled(True)

    def import_keys_rsa(self):
        """This method allows user to choose files with public and private keys
        for RSA signing algorithm
        """
        self.cipher = RSAcipher.RSA(512)

        private = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл закрытого ключа", filter="*.privrsa"
        )[0]

        public = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл открытого ключа", filter="*.pubrsa"
        )[0]
        self.textBrowserKeysRSA.clear()
        self.cipher.import_keys(private, public)
        if private:
            self.btnSignFileRSA.setEnabled(True)
            self.textBrowserKeysRSA.append(f"PRIVATE KEY:\n"
                                           f"d = {self.cipher.public_key[0]}\n"
                                           f"n = {self.cipher.public_key[1]}\n")
        else:
            self.btnSignFileRSA.setEnabled(False)
        if public:
            self.textBrowserKeysRSA.append(
                f"PUBLIC KEY:\ne = {self.cipher.private_key[0]}\n"
                f"n = {self.cipher.private_key[1]}\n"
            )
            self.btnCheckSignRSA.setEnabled(True)
        else:
            self.btnCheckSignRSA.setEnabled(False)

    def sign_file_rsa(self):
        """This method allows user to generate file's signature
         using RSA algorithm
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл для подписи"
        )

        if file[0]:
            with open(file[0], "rb") as f:
                message = f.read()
            message_hash = int(sha512(message).hexdigest(), 16)
            self.signRSA = self.cipher.encrypt(message_hash)
            self.textBrowserSignRSA.setText(f"Подпись RSA: {self.signRSA}")
            self.btnSaveSignRSA.setEnabled(True)

    def save_sign_rsa(self):
        """This method allows user to save signature to the file
        """
        file = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохранить как", filter="*.rsasign"
        )

        if file[0]:
            with open(file[0], "w") as f:
                f.write(f"{self.signRSA}")

    def check_sign_rsa(self):
        """This function provides sign checking with RSA algorithm
        """

        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл"
        )

        sign = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл с подписью", filter="*.rsasign"
        )

        if file[0] and sign[0]:
            try:
                with open(file[0], "rb") as f:
                    message = f.read()
                message_hash = int(sha512(message).hexdigest(), 16)
            except Exception:
                self.textBrowserSignRSA.setText("1")
                return

            try:
                with open(sign[0], "r") as f:
                    sign = int(f.read())
                sign_hash = self.cipher.decrypt(sign)
            except Exception:
                self.textBrowserSignRSA.setText("2")
                return
            if message_hash == sign_hash:
                self.textBrowserSignRSA.setText("Подпись верна")
            else:
                self.textBrowserSignRSA.setText("Подпись неверна")

    def generate_random_elgamal(self):
        """This function generates random numbers for El Gamal signing
        """
        nums = crypto_numbers.get_dh_nums(512)
        self.public_elgamal['p'] = nums[0]
        self.public_elgamal['g'] = nums[1]
        self.lineEditPElGamal.setText(f"{self.public_elgamal['p']}")
        self.lineEditGElGamal.setText(f"{self.public_elgamal['g']}")
        self.btnFindG.setEnabled(True)
        self.btnGenerateKeysElGamal.setEnabled(True)

    def choose_pfile_elgamal(self):
        """This function provides user to choose file with number P for El Gamal
         signing
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл", filter="*.txt"
        )[0]

        if file:
            try:
                with open(file, "r") as f:
                    self.public_elgamal['p'] = int(f.read().strip())
                self.lineEditPElGamal.setText(f"{self.public_elgamal['p']}")
                self.btnFindG.setEnabled(True)
                self.btnChooseGFileElGamal.setEnabled(True)
            except Exception:
                self.lineEditPElGamal.setText("Something went wrong reading file")

    def choose_gfile_elgamal(self):
        """This function provides user to choose file with number G for El Gamal
        signing
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл", filter="*.txt"
        )[0]

        if file:
            try:
                with open(file, 'r') as f:
                    self.public_elgamal['g'] = int(f.read().strip())
                self.lineEditGElGamal.setText(f"{self.public_elgamal['g']}")
                self.btnGenerateKeysElGamal.setEnabled(True)
            except Exception:
                self.lineEditGElGamal.setText("Someting went wrong reading file")

    def generate_keys_elgamal(self):
        """This function does key generation for El Gamal signing
        """
        self.private_elgamal = random.randint(0, self.public_elgamal['p'] - 1)
        self.public_elgamal['y'] = pow(self.public_elgamal['g'],
                                        self.private_elgamal,
                                        self.public_elgamal['p'])
        self.textBrowserKeysElGamal.setText(f"PUBLIC:\n"
                                            f"y = {self.public_elgamal['y']}\n"
                                            f"g = {self.public_elgamal['g']}\n"
                                            f"p = {self.public_elgamal['p']}\n"
                                            f"PRIVATE:\n"
                                            f"x = {self.private_elgamal}")

        self.btnSignFileElGamal.setEnabled(True)
        self.btnCheckSignElGamal.setEnabled(True)

        public = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохранить открытый ключ как", filter="*.pubel"
        )[0]
        private = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохранить закрытый ключ как", filter="*.privel"
        )[0]

        if public and private:
            with open(public, "w") as f:
                f.write(f"{self.public_elgamal['y']}\n"
                        f"{self.public_elgamal['g']}\n"
                        f"{self.public_elgamal['p']}\n")
            with open(private, 'w') as f:
                f.write(f"{self.private_elgamal}")

    def import_keys_elgamal(self):
        """This method is used to import keys for El Gamal signing from file
        """
        public = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл", filter="*.pubel"
        )[0]
        private = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл", filter="*.privel"
        )[0]
        flag = False
        if public:
            try:
                with open(public, 'r') as f:
                    t = f.readlines()
                self.public_elgamal['y'] = int(t[0].strip())
                self.public_elgamal['g'] = int(t[1].strip())
                self.public_elgamal['p'] = int(t[2].strip())
                flag = True
                self.btnCheckSignElGamal.setEnabled(True)
            except Exception:
                return

        if private:
            try:
                with open(private, 'r') as f:
                    self.private_elgamal = int(f.read().strip())
                self.btnSignFileElGamal.setEnabled(flag)
            except Exception:
                return

    def sign_file_elgamal(self):
        """This function generates file's sign by El Gamal algorithm
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл"
        )[0]
        if file:
            with open(file, "rb") as f:
                text = f.read()
            message = int(sha512(text).hexdigest(), 16)
        else:
            return

        k = 0
        res = {'reminder': 0}
        while res['reminder'] != 1:
            k = random.randint(0, self.public_elgamal['p'] - 1)
            res = crypto_numbers.gcd(k, self.public_elgamal['p'] - 1)
        a = pow(self.public_elgamal['g'], k, self.public_elgamal['p'])
        t = message - self.private_elgamal * a
        b = (res['x'] * t) % (self.public_elgamal['p'] - 1)
        self.signElGamal = (a, b)
        self.textBrowserSignElGamal.setText(f"Sign:\n"
                                            f"a = {a}"
                                            f"b = {b}")
        self.btnSaveSignElGamal.setEnabled(True)

    def save_sign_elgamal(self):
        """This function provides saving the electronic sign to the file
        """
        file = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Сохранить подпись как", filter="*.elsign"
        )[0]

        if file:
            with open(file, 'w') as f:
                f.write(f"{self.signElGamal[0]}\n"
                        f"{self.signElGamal[1]}")

    def check_sign_elgamal(self):
        """This function checks El Gamal sign of the file
        """
        file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл"
        )[0]

        sign = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите подпись", filter="*.elsign"
        )[0]

        if file and sign:
            with open(file, "rb") as f:
                text = f.read()
            hash_text = int(sha512(text).hexdigest(), 16)

            with open(sign, "r") as f:
                t = f.readlines()
            a = int(t[0])
            b = int(t[1])
            sign = pow(self.public_elgamal['y'], a, self.public_elgamal['p'])
            sign = (sign * pow(a, b, self.public_elgamal['p'])) % self.public_elgamal['p']
            hash_text = pow(self.public_elgamal['g'], hash_text, self.public_elgamal['p'])
            if sign == hash_text:
                self.textBrowserSignElGamal.setText("Подпись верна")
            else:
                self.textBrowserSignElGamal.setText("Подпись неверна")
