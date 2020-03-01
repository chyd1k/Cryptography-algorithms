import random
from PyQt5 import QtWidgets
from XOR import LFSR
from ChiSqr import ChiSqr_interface


class ChiSqrApp(QtWidgets.QMainWindow,
                ChiSqr_interface.Ui_MainWindow):
    """This class implements application that perform the chi-square test for
    the LFSR built on given polynomial
    More about test:
    https://en.wikipedia.org/wiki/Chi-squared_test
    Also this application finds the LFSR's period
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.polynom = []
        self.root = None
        self.scrembler = None

        self.btnTest.clicked.connect(self.test)

    def test(self):
        """This function actually performs test
        """
        self.polynom = list(map(
            int, self.lineEditPolynom.text().split(" ")
        ))

        try:
            self.root = int(self.lineEditRoot.text())
        except Exception:
            self.root = None
            self.textBrowserResult.setText("Wrong initial root value")
        if not self.root:
            self.root = random.randint(0, 2 ** int(self.polynom[0]) - 1)
        self.scrembler = LFSR.LFSR(self.polynom, self.root)

        self.textBrowserResult.setText(f"Полином: {self.scrembler.polynom}"
                                       f"\nНачальное значение:"
                                       f" {self.scrembler.root}")

        max_Value = 2 ** self.scrembler.size - 1
        self.textBrowserResult.append(
            f"Минимальное значение: 0\t"
            f"Максимальное значение: {max_Value}"
        )

        interval_count = 100
        while max_Value % interval_count != 0:
            interval_count -= 1
        step = max_Value // interval_count
        intervals = {}
        for i in range(0, max_Value, step):
            intervals[f"{i}-{i + step}"] = 0
        self.textBrowserResult.append(
            f"Разбиваем весь отрезок на {interval_count} интервалов "
            f"по {step}"
        )

        n = 10 * interval_count
        self.textBrowserResult.append(
            f"Количество генерируемых чисел: {n}"
        )
        roots = []
        flag = True
        for i in range(n):
            roots.append(self.scrembler.root)
            list(self.scrembler.get_bits(1))
            if flag:
                self.textBrowserResult.append(
                    f"{roots[i]}"
                )
                new_root = self.scrembler.root
                if new_root in roots:
                    self.textBrowserResult.append(
                        f"{new_root}\n"
                        f"Зацикливание последовательности после "
                        f"{i} сгенерированных чисел"
                    )
                    flag = False
        if flag:
            self.textBrowserResult.append("Зацикливание последовательности "
                                          "среди сгенерированных чисел не "
                                          "найдено.")
        self.textBrowserResult.append(
            f"\nТеперь считаем Хи-квадрат"
        )
        for root in roots:
            for key in intervals.keys():
                if root >= int(key.split("-")[0]):
                    if root < int(key.split("-")[1]):
                        intervals[key] += 1
        s = 0
        for key in intervals.keys():
            s += intervals[key] ** 2 / (1 / interval_count)
        hisqr = 1 / n * s - n
        v = n - 1
        theoretical = v - 2 / 3 + 1 / (v ** 0.5)
        proc = theoretical * 2
        proc = hisqr / (proc / 100)
        self.textBrowserResult.append(
            f"Показатель Хи-квадрат практический: {hisqr}\n"
            f"Теоретический для равномерного распределения: {theoretical}\n"
            f"Процентная точка распределения: {proc}%"
        )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ChiSqrApp()
    window.show()
    app.exec_()
