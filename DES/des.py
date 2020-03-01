from random import getrandbits
from PyQt5 import QtWidgets
from DES.lab4_interface import *
import sys
from DES import feist
from DES.Avalanche import AvalancheApp

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.encrypt)
        self.ui.pushButton_2.clicked.connect(self.decrypt)
        self.ui.pushButton_3.clicked.connect(self.choose_text_file)
        self.ui.pushButton_4.clicked.connect(self.choose_key_file)
        self.ui.pushButton_5.clicked.connect(lambda : AvalancheApp(self).show())
        #self.ui.pushButton_5.clicked.connect(self.Avalanche_effect)

        self.ui.radioButton.clicked.connect(self.to_hex)
        self.ui.radioButton_2.clicked.connect(self.to_symbols)

        self.ui.radioButton_4.setChecked(True)
        self.mode = 1

        self.ui.radioButton_3.clicked.connect(self.CBC_mode)
        self.ui.radioButton_4.clicked.connect(self.ECB_mode)
        self.ui.radioButton_5.clicked.connect(self.CFB_mode)
        self.ui.radioButton_6.clicked.connect(self.OFB_mode)
        self.ui.radioButton_7.clicked.connect(self.BC_mode)
        self.ui.radioButton_8.clicked.connect(self.PCBC_mode)
        self.ui.radioButton_9.clicked.connect(self.OFBNLF_mode)

        self.ui.radioButton_12.clicked.connect(self.DBL_mode)
        self.ui.radioButton_11.clicked.connect(self.DEV_PR_mode)
        self.ui.radioButton_13.clicked.connect(self.TACHMEN_EDE_mode)
        self.ui.radioButton_10.clicked.connect(self.TRPL_mode)

        self.initialialize_vector = 5182229638493943934
        self.keys = []
        self.inText = ''
        self.outText = ''


    def Avalanche_effect(self):
        mes = self.inText
        while (len(mes) % 64) != 0:
            mes = '0' + mes
        blocks_count = len(feist.block64bits(mes))
        #print(mes)
        #print(self.outText)
        res = 0
        for i in range(len(mes)):
            if mes[i] == '1':
                str = mes[:i] + '0' + mes[i+1:]
            elif mes[i] == '0':
                str = mes[:i] + '1' + mes[i+1:]
            encbits_av = feist.encode(self.mode, self.initialialize_vector, str, 16, self.keys)[1]
            temp = f'{bin(int(encbits_av, 2) ^ int(self.outText, 2))[2:]}'
            #print(f'{temp}')
            sum = 0
            for j in temp:
                if j == '1':
                    sum += 1
            #print(f'{sum}\n')
            res += sum
            #print(f'Change bit № {i} Bits changed in encrypted message {sum}')
        avr_b = res / (64 * blocks_count)
        print(f'Average number of changed bits : {avr_b}')
        print(f'Percentage of bits changed : {(avr_b / len(mes)) * 100}%\n')


    def CBC_mode(self):
        self.mode = 2

    def ECB_mode(self):
        self.mode = 1

    def CFB_mode(self):
        self.mode = 3

    def OFB_mode(self):
        self.mode = 4

    def PCBC_mode(self):
        self.mode = 5

    def BC_mode(self):
        self.mode = 6

    def OFBNLF_mode(self):
        self.mode = 7

    def DBL_mode(self):
        self.mode = 8

    def DEV_PR_mode(self):
        self.mode = 9

    def TACHMEN_EDE_mode(self):
        self.mode = 10

    def TRPL_mode(self):
        self.mode = 11

    def anymsg2bin(self):
        message = self.ui.textBrowser.toPlainText()
        if message[:2] == '0x':
            try:
                message = str(bin(int(message, 16))[2:])
                #print(f'message in hex')
                self.ui.textBrowser.setText(f'{message}')
            except Exception:
                pass
                #print("Can't make int")
        try:
            temp = int(message, 2)
            #print(f'Message already in bin')
        except Exception:
            if message.isdigit():
                #print('Message in integer')
                message = str(bin(int(message))[2:])
                #print(f'message in int')
                self.ui.textBrowser.setText(f'{message}')
            else:
                #print('Message in string')
                mesinbytes = message.encode()
                mesinint = int.from_bytes(mesinbytes, 'big')
                message = str(bin(mesinint)[2:])
                self.ui.textBrowser.setText(f'{message}')

    def to_hex(self):
        message = self.ui.textBrowser_2.toPlainText()
        mesinbytes = message.encode()
        mesinint = int.from_bytes(mesinbytes, 'big')
        mesinbin = bin(mesinint)[2:]

        if message[:2] == '0x':
            pass
            #print('Already in hex')
        else:
            try:
                message1 = int(message, 2)
                #print(f'Message in bin')
                self.ui.textBrowser_2.setText(f'{hex(int(message, 2))}')
            except Exception:
                if message.isdigit():
                    self.ui.textBrowser_2.setText(f'{hex(int(message))}')
                    #print(f'Message in integer')
                else:
                    #print(f'Message in text')
                    message = message.encode('utf-8')
                    self.ui.textBrowser_2.setText(f'{"0x"+message.hex()}')

    def to_symbols(self):
        message = self.ui.textBrowser_2.toPlainText()
        if message[:2] == '0x':
            try:
                print(message)
                message = int(message, 16)
                print(message)
                print(message.to_bytes(message.bit_length(), "big").decode())
                #print(message.to_bytes(message.bit_length(), "big").decode())
                self.ui.textBrowser_2.setText(message.to_bytes(message.bit_length(), "big").decode())
            except Exception:
                pass
                #print("Can't decode bytes")
        elif message.isdigit():
            #print('Message in integer')
            message = int(message)
            try:
                message = message.to_bytes(message.bit_length(), "big").decode()
                #print('Decoded  from int to string')
            except Exception:
                pass
                #print("Can't decode bytes")
        #else:
            #pass
            #print('Message in string')


    def choose_text_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл с сообщением для шифрования/дешифрования", filter="*.txt")
        if file[0]:
            with open(file[0], "r") as f:
                x = f.read().encode()

        try:
            mestoenc = x.decode()
            self.ui.textBrowser.setText(mestoenc)

        except Exception:
            mestoenc = hex(int.from_bytes(x, "big"))
            print('asdasd' +str(int.from_bytes(x, "big")))
            self.ui.textBrowser.setText(mestoenc)

    def choose_key_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл с ключом", filter="*.txt")
        if file[0]:
            with open(file[0], 'r') as f:
                self.keys = list(map(int, f.readlines()))
            #with open(file[0], "rb") as f:
                #self.inText = f.read()
        #key = self.inText.decode()
        self.ui.lineEdit.setText(str(self.keys).replace(',',' ')[1:-1])

    def encrypt(self):
        message = self.ui.textBrowser.toPlainText()
        mesinbytes = message.encode()
        mesinint = int.from_bytes(mesinbytes, 'big')
        message = bin(mesinint)[2:]
        self.inText = message
        encmes, encbits = feist.encode(self.mode, self.initialialize_vector, message, 16, self.keys)
        self.outText = encbits
        self.ui.textBrowser_2.setText(f'{encmes}')
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл для сохранения зашифрованного сообщения", filter="*.txt")

        if file[0]:
            f = open(file[0], 'w')
            f.write(encbits)
            f.close()
        return encmes

    def decrypt(self):
        self.anymsg2bin()
        message = self.ui.textBrowser.toPlainText()
        key = self.ui.lineEdit.text()
        decmes, decbits = feist.decode(self.mode, self.initialialize_vector, message, 16, self.keys)
        #self.outText = decbits
        self.ui.textBrowser_2.setText(f'{decmes}\n')
        return decbits, decmes

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
