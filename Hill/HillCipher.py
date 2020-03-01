import crypto_numbers
from Hill import Matrix


class Hill:
    """This class implements Hill cipher
    """
    # Алфавит
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" \
              "!\"#$%&'()*+,-./:;<=>?@[\]^_`" \
              " АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
    # Размер алфавита
    size = len(symbols)

    def __init__(self):
        self.block_size = 0
        self.key = 0
        self.rev_key = 0

    def setKeyword(self, keyword) -> bool:
        """This function sets the key

        Args:
            keyword -- text to be converted to the key

        Return: True if the key set successfully, else - False
        """
        self.block_size = 0
        for i in range(len(keyword)):
            if i**2 == len(keyword):
                self.block_size = i
                break
        if self.block_size == 0:
            return False

        self.key = Matrix.Matrix(self.block_size, self.block_size)
        for i in range(self.block_size):
            for j in range(self.block_size):
                self.key[i][j] = Hill.symbols.find(
                    keyword[self.block_size*i + j]
                )
        det = self.key.determinant()
        if crypto_numbers.gcd(det, Hill.size)["reminder"] != 1:
            return False
        obr_det = crypto_numbers.gcd(
            self.key.determinant(), self.size)["x"] % self.size
        self.rev_key = (self.key.algebDop().transp() * obr_det) % self.size
        return True

    def encrypt(self, plain_text) -> str:
        """This function provides text encryption

        Args:
            plain_text -- text to be encrypted

        Return: processed text
        """
        while len(plain_text) % self.block_size != 0:
            plain_text += " "
        
        cipher_text = []
        for i in range(len(plain_text)//self.block_size):
            cipher_text.append(Matrix.Matrix(1, self.block_size))
            for j in range(self.block_size):
                cipher_text[i][0][j] = Hill.symbols.find(
                    plain_text[self.block_size * i + j]
                )
        
        for i in range(len(cipher_text)):
            cipher_text[i] = (cipher_text[i] * self.key) % self.size
        
        result = ""

        for i in range(len(cipher_text)):
            for j in range(self.block_size):
                result += Hill.symbols[cipher_text[i][0][j]]
        return result
    
    def decrypt(self, cipher_text):
        """This function provides decryption

        Args:
            cipher_text -- text to be decrypted

        Return: processed text
        """
        plain_text = []
        for i in range(len(cipher_text)//self.block_size):
            plain_text.append(Matrix.Matrix(1, self.block_size))
            for j in range(self.block_size):
                plain_text[i][0][j] = Hill.symbols.find(
                    cipher_text[self.block_size * i + j]
                )

        for i in range(len(plain_text)):
            plain_text[i] = (plain_text[i] * self.rev_key) % self.size
        
        result = ""

        for i in range(len(plain_text)):
            for j in range(self.block_size):
                result += Hill.symbols[plain_text[i][0][j]]
        return result

    @staticmethod
    def test():
        h = Hill()
        keyword = input("Введите ключ (длина равна квадрату целого числа): ")
        h.setKeyword(keyword)
        text = input("Введите текст для шифрования: ")
        text = h.encrypt(text)
        print("Шифротекст: " + text)
        text = h.decrypt(text)
        print("Открытый текст: " + text)


if __name__ == "__main__":
    Hill.test()
