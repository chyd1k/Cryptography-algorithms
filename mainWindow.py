from PyQt5 import QtWidgets
import mainWindow_interface
from DiffieHellman import DiffieHellman
from PrimitiveRoots import PrimitiveRoots
from PrimeNumbers import PrimeNumbers
from Hill import Hill
from Feistel import Feistel
from XOR import XOR
from ChiSqr import ChiSqr
from DES import des
from RSA import RSA
from Hash import Hash


class mainWindowApp(QtWidgets.QMainWindow,
                    mainWindow_interface.Ui_MainWindow):
    """This class implements main window of the application
    Nothing interesting happens in it's methods. Every button calls new window
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnPrimitiveRoots.clicked.connect(self.initPrimitiveRoots)
        self.btnGenPrime.clicked.connect(self.initGenPrime)
        self.btnDiffieHellman.clicked.connect(self.initDiffieHellman)
        self.btnHill.clicked.connect(self.initHill)
        self.btnFeistel.clicked.connect(self.initFeistel)
        self.btnXor.clicked.connect(self.initXor)
        self.btnHiSqr.clicked.connect(self.initHiSqr)
        self.btnDes.clicked.connect(self.initDes)
        self.btnRSA.clicked.connect(self.initRSA)
        self.btnHash.clicked.connect(self.initHash)

    def initPrimitiveRoots(self):
        new_window = PrimitiveRoots.PrimitiveRootsApp(self)
        new_window.show()

    def initGenPrime(self):
        new_window = PrimeNumbers.PrimeNumbersApp(self)
        new_window.show()

    def initDiffieHellman(self):
        new_window = DiffieHellman.Diffie_HellmanApp(self)
        new_window.show()

    def initHill(self):
        new_window = Hill.HillApp(self)
        new_window.show()

    def initFeistel(self):
        new_window = Feistel.FeistelApp(self)
        new_window.show()

    def initXor(self):
        new_window = XOR.XORApp(self)
        new_window.show()

    def initHiSqr(self):
        new_window = ChiSqr.ChiSqrApp(self)
        new_window.show()

    def initDes(self):
        new_window = des.MyWin(self)
        new_window.show()

    def initRSA(self):
        new_window = RSA.RSAApp(self)
        new_window.show()

    def initHash(self):
        new_window = Hash.HashApp(self)
        new_window.show()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindowApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
