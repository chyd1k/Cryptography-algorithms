from datetime import datetime
from PyQt5 import QtWidgets
import crypto_numbers
from DiffieHellman import Diffie_Hellman_interface


class Diffie_HellmanApp(QtWidgets.QMainWindow,
                        Diffie_Hellman_interface.Ui_MainWindow):
    """This class implements application that simulates Diffie-Hellman protocol
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.n = 0
        self.g = 0
        self.xA = None
        self.xB = None
        self.yA = None
        self.yB = None
        self.K = None

        self.btnGenerateRand.clicked.connect(self.generateRand)
        self.btnSimulate.clicked.connect(self.simulate)

    def generateRand(self):
        """This function generates random 40 bit number which is used as public
        key
        """
        start = datetime.now()
        try:
            length = int(self.lineEditKeyLength.text())
        except Exception:
            return
        self.n, self.g = crypto_numbers.get_dh_nums(length)
        end = datetime.now()
        self.textBrowser.setText(f"Время генерации: {end-start}")
        self.lineEditN.setText(str(self.n))
        self.lineEditG.setText(str(self.g))

    def simulate(self):
        """This function actually simulates Diffie-Hellman protocol
        """
        import random
        self.textBrowser.clear()
        try:
            self.xA = int(self.lineEditXA.text())
        except Exception:
            self.textBrowser.append("Не введен X для абонента А, либо"
                                    " его невозможно считать. Он будет"
                                    " сгенерирован автоматически.")
            self.xA = random.randint(2, self.n)
            self.lineEditXA.setText(str(self.xA))
        try:
            self.xB = int(self.lineEditXB.text())
        except Exception:
            self.textBrowser.append("Не введен Х для абонента Б, либо"
                                    " его невозможно считать. Он будет"
                                    " сгенерирован автоматически.")
            self.xB = random.randint(2, self.n)
            self.lineEditXB.setText(str(self.xB))

        self.yA = pow(self.g, self.xA, self.n)
        self.yB = pow(self.g, self.xB, self.n)

        self.textBrowser.append(f"\nАбонент А вычисляет Y: Ya = g^X mod n ="
                                f" {self.g}^{self.xA} mod {self.n} = {self.yA}"
                                f"\tАбонент B вычисляет Y: Yb = g^X mod n ="
                                f" {self.g}^{self.xB} mod {self.n} = {self.yB}")
        self.textBrowser.append(f"\nАбоненты обмениваются значениями Y")
        self.K = pow(self.yA, self.xB, self.n)
        self.textBrowser.append(f"\nАбонент А вычисляет K: K = Yb^Xa mod n ="
                                f" {self.yB}^{self.xA} mod {self.n} = "
                                f"{pow(self.yB, self.xA, self.n)}"
                                f"\tАбонент B вычисляет K: K = Ya^Xb mod n ="
                                f" {self.yA}^{self.xB} mod {self.n} = "
                                f"{pow(self.yA, self.xB, self.n)}")


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Diffie_HellmanApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
