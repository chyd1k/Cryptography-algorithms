from PyQt5 import QtWidgets
import crypto_numbers
from PrimitiveRoots import PrimitiveRoots_interface


class PrimitiveRootsApp(QtWidgets.QMainWindow,
                        PrimitiveRoots_interface.Ui_MainWindow):
    """This class implements application that finds first 100 primitive roots
    of given modulo. Although there might be less then 100 of them. It depends
    on modulo."""
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)

        self.btnFind.clicked.connect(self.primitive_roots)

    def primitive_roots(self):
        """Function finds primitive root modulo n

        Args:
            n -- modulo

        Return: integer wich is primitive root or None if nothing found
        """
        from datetime import datetime
        try:
            n = int(self.lineEditN.text())

        except Exception:
            return

        if n <= 0:
            self.textBrowserPrimitiveRoots.setText("Число должно быть больше 0")
            return
        if n <= 2:
            return
        phi = crypto_numbers.euler_func(n)
        phi_factors = crypto_numbers.prime_factors(phi)
        result = ""
        i = 0
        start = datetime.now()
        for g in range(2, n + 1):
            check = True
            for p in phi_factors:
                check &= pow(g, phi // p, n) != 1
            if check:
                result += f"{g} "
                i += 1
            if i >= 100:
                break
        end = datetime.now()
        self.textBrowserPrimitiveRoots.setText(
            f"Первые 100 первообразных корней по модулю {n}:{result}"
            f"\nЗатраченное время: {end - start}"
        )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PrimitiveRootsApp()
    window.show()
    app.exec_()
