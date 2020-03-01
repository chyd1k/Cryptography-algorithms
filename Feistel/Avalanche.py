from PyQt5 import QtWidgets
from Feistel import Avalanche_interface


class AvalancheApp(QtWidgets.QMainWindow,
                   Avalanche_interface.Ui_MainWindow):
    """This is not standalone class. It is designed to be a child of Feistel
    class
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        # inText and outText store plain text and encrypted text as bits
        self.blocks_in = parent.cipher.slice(parent.inText)
        self.blocks_out = parent.cipher.slice(parent.outText)
        self.inText = None
        self.outText = None
        self.block_count = len(self.blocks_in)
        self.block_num = None
        self.d1 = 0
        self.lblBlockCount.setText(
            self.lblBlockCount.text() + f"{self.block_count}"
        )

        # self.lineEditInText.setText(self.inText)
        # self.lineEditOutText.setText(self.outText)

        self.btnProcess.clicked.connect(self.oneBit)
        self.btnAverage.clicked.connect(self.average)
        self.btnChooseBlock.clicked.connect(self.chooseBlock)
        self.btnBlocksAverage.clicked.connect(self.averageBlocks)

    def chooseBlock(self):
        """This function provides block choosing among the whole text
        """
        try:
            self.block_num = int(self.lineEditBlockNum.text())
            self.inText = self.blocks_in[self.block_num]
            self.outText = self.blocks_out[self.block_num]
            self.lineEditInText.setText(self.inText)
            self.lineEditOutText.setText(self.outText)
        except Exception:
            return

    def averageBlocks(self):
        """This method calculates chi sqr parameter for the whole text
        """
        for i in range(self.block_count):
            self.inText = self.blocks_in[i]
            self.outText = self.blocks_out[i]
            self.average()
        self.d1 = self.d1 / self.block_count
        self.d1 = self.d1 / len(self.inText)
        self.textEditResults.setText(f"Среднее число: {self.d1}")

    def process(self, index: int):
        """
        This method is being used to test avalanche effect of the cipher. It
        changes bit in given index. Bits are being indexed from lowest to
        highest, so it's right to left


        Args:
            index - index of bit to be inverted

        Return: count of bits in encrypted text changed with one bit changed in
        plain text
        """
        index = len(self.inText) - index - 1

        text = self.inText
        if text[index] == '0':
            text = text[:index] + "1" + text[index + 1:]
        else:
            text = text[:index] + "0" + text[index + 1:]

        old_out_text = self.outText

        new_out_text = int(text, 2)
        new_out_text = new_out_text.to_bytes(
            new_out_text.bit_length(), "big"
        )
        new_out_text = self.parent().cipher.process(
            new_out_text, self.parent().black_box, False
        )
        new_out_text = self.parent().cipher.slice(new_out_text)[0]

        old_out_text = list(old_out_text)
        new_out_text = list(new_out_text)
        count = 0
        changes = []
        for i in range(len(old_out_text)):
            if new_out_text[i] != old_out_text[i]:
                count += 1
                changes.append(i)
                new_out_text[i] = f"<b><font color='red'>{new_out_text[i]}</font></b>"
            old_out_text[i] = f"<b><font color='blue'>{old_out_text[i]}</font></b>"
        new_out_text = "".join(new_out_text)
        old_out_text = "".join(old_out_text)

        self.textEditResults.insertHtml(
            f"<div>"
            f"<p>"
            f"<b>Изменяем бит номер {len(self.inText) - index - 1}</b></p>"
            f"<p>Входной текст: </p>"
            f"<p align='center'><b>До</b></p>"
            f"<p align='center'>{self.inText[:index]}"
            f"<b><font color='blue'>{self.inText[index]}</font></b>"
            f"{self.inText[index + 1:]}</p>"
            f"<p align='center'><b>После</b></p>"
            f"<p align='center'>{text[:index]}"
            f"<b><font color='red'>{text[index]}</font></b>"
            f"{text[index + 1:]}</p>"
            f"<p>Выходной текст: </p>"
            f"<p align='center'><b>До</b></p>"
            f"<p align='center'>{old_out_text}</p>"
            f"<p align='center'><b>После</b></p>"
            f"<p align='center'>{new_out_text}</p>"
            f"<p>Количество изменившихся бит: <b>{count}</b></p>"
            f"<p align='center'><b>{'_'*len(self.inText)}</b></p>"
            f"</div>"
            f"<pre>\n</pre>"
        )
        return count

    def oneBit(self):
        """This function inverts one bit of the block on index chosen by user
        """
        try:
            index = int(self.lineEditIndex.text())
        except Exception:
            return
        self.textEditResults.clear()
        self.process(index)

    def average(self):
        """This method inverts all bits of the block one by one and calculates
        average chi sqr parameter
        """
        self.textEditResults.clear()
        count = 0
        for i in range(len(self.inText)):
            count += self.process(i)
        self.textEditResults.append(
            f"\nСреднее количество меняющихся бит: {count/len(self.inText)}"
        )
        self.d1 += count


if __name__ == "__main__":
    print("Can't be called as standalone application")
    input()
