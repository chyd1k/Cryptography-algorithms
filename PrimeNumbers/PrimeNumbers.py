import random
from datetime import datetime
from PyQt5 import QtWidgets
from PrimeNumbers import PrimeNumbers_interface


class PrimeNumbersApp(QtWidgets.QMainWindow,
                      PrimeNumbers_interface.Ui_MainWindow):
    """This class implements application that generates prime numbers with
    given bit length. Also it finds all prime numbers in the given range
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnGeneratePrime.clicked.connect(self.get_prime)
        self.btnRange.clicked.connect(self.get_range)

    def is_prime(self, p: int, t: int = 10):
        """Miller-Rabin primality test. Error probability is (1/4)^t
        More about Miller-Rabin test:
        https://en.wikipedia.org/wiki/Miller–Rabin_primality_test

        Args:
            p -- number to be tested
            t -- count of tests

        Return: True if the number is prime, else - False
        """
        temp = p - 1
        b = 0
        while temp % 2 == 0:
            temp = temp // 2
            b += 1
        m = (p - 1) // 2 ** b
        for i in range(t):
            a = random.randint(2, p - 1)
            z = pow(a, m, p)
            if z == 1 or z == p - 1:
                continue

            for j in range(b - 1):
                z = pow(z, 2, p)
                if z == 1:
                    return False
                elif z == p - 1:
                    break
            if z == p - 1:
                continue
            else:
                return False
        return True

    def get_prime(self):
        """Function generates random prime number with bit length equals n
        """
        self.textBrowserPrime.clear()
        start = datetime.now()
        try:
            n = int(self.lineEditBitLength.text())
            t = int(self.lineEditTests.text())
            i = 0
        except Exception:
            pass
        else:
            while True:
                if n <= 1 or t < 1:
                    return
                i += 1
                # Here I use random.getrandbits to generate n random bits
                # Although higher bits might be 0, so actually this number
                #  may have bit length less then n.
                # Moreover, lowest bit might be 0, so
                # this number is not prime
                # To fix this I switch lowest bit to 1, and after that, while
                # the bit length of number less than n I
                # complete it with 1 and 0.
                # For example, n = 4, but generated 0010, so it's 2.
                # And actual bit length is 2 (10). So I do this:
                # 1) Switch lowest bit to 1 and I get number 3 -> 11
                # 2) Complete number to 4 bits, so that highest bit is 1
                #   11 -> 1011
                bits = list(bin(random.getrandbits(n))[2:])
                bits[-1] = "1"
                while len(bits) < n:
                    bits.insert(0, "0")
                bits[0] = "1"
                num = int("".join(bits), 2)

                # Now I has actual n bits number, but I cant say it's prime
                # So I check it
                # First, I check if the number is divisible by any of prime
                # numbers from 2 to 200
                little_primes = [
                    2, 3, 5, 7, 11, 13, 17, 19,
                    23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79,
                    83, 89, 97, 101, 103, 107,
                    109, 113, 127, 131, 139, 149,
                    151, 157, 163, 167, 173, 179,
                    181, 191, 193, 197, 199
                ]
                little_checks = [
                    num % p == 0 and num != p for p in little_primes
                ]
                if True in little_checks:
                    continue

                # If it's not, I run Miller-Rabin test 10 times for this number
                # If number passes the test I return it. And it's prime with the
                # probability of 0.9999990463256836

                if self.is_prime(num, t):
                    end = datetime.now()
                    self.textBrowserPrime.append(
                        f"Сгенерированное число: {num}\n"
                        f"Количество итераций затрачено: {i}\n"
                        f"Затраченное время: {end - start}\n"
                        f"Сгенерированное число"
                        f" НЕ простое с вероятностью: {1/4**t}"
                    )
                    break

    def get_range(self):
        """Function finds all prime numbers in the given range
        """
        self.textBrowserRange.clear()
        try:
            a = int(self.lineEditLow.text())
            b = int(self.lineEditHigh.text())
        except Exception:
            return
        else:
            start = datetime.now()
            res = ""
            if a < 0 or b < 0:
                self.textBrowserRange.append("Числа должны быть больше 0")
                return
            if a <= 2:
                res += "2 "
                a = 3
            if a % 2 == 0:
                a += 1
            if b < a:
                return
            if b % 2 == 0:
                b -= 1
            for i in range(a, b + 1, 2):
                if self.is_prime(i):
                    res += f"{i} "
            end = datetime.now()
            self.textBrowserRange.append(res)
            self.textBrowserRange.append(f"Затраченное время: {end - start}")


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PrimeNumbersApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
