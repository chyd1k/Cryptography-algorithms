import textwrap
from XOR import LFSR


class Feistel:
    """This class implements Feistel cipher"""

    def __init__(self, key: int = None,
                 blocksize: int = 64,
                 rounds_count: int = 8,
                 generation_method: int = 1):
        """Creates a class object

        Keyword arguments:
        key -- cipher key, being used to generate round keys
        blocksize -- bit length of one text block
        rounds_count -- count of procession rounds to do
        generation_method -- pointer that defines a function to
         use for round keys generation"""
        t = blocksize
        if t % 2 != 0:
            raise ValueError(
                "Blocksize must be 2^i, where i is positive integer"
            )
        else:
            while t % 2 == 0 and t != 1:
                t = t // 2
            if t != 1:
                raise ValueError(
                    "Blocksize must be 2^i, where i is positive integer"
                )
        self.blocksize = blocksize

        if not key:
            import random
            self.key = random.getrandbits(blocksize)
        else:
            self.key = key

        self.rounds_count = rounds_count
        if generation_method == 1:
            self.round_keys = self.generate_round_keys()
        elif generation_method == 2:
            self.round_keys = self.generate_round_keys_a()
        else:
            ValueError("No such generation method")

    def black_box_a(self, a, b):
        """This and other black boxes is being used in
        the cipher. Every black box should take two parameters, but thats
        not necessary to use both of them

        Args:
        a - left part of the text
        b - round key"""
        return b

    def black_box_b(self, a, b) -> int:
        """This and other black boxes is being used in
        the cipher. Every black box should take two parameters, but thats
        not necessary to use both of them

        Args:
        a - left part of the text
        b - round key

        Return: integer value"""
        polynom = [16, 14, 1, 0]
        scrembler = LFSR.LFSR(polynom=polynom)
        rand_bits = int(
            "".join(
                map(
                    str, list(scrembler.get_bits(self.blocksize // 2))
                )), 2)
        return a ^ rand_bits ^ b

    def black_box(self, a, b) -> int:
        """This and other black boxes is being used in
        the cipher. Every black box should take two parameters, but thats
        not necessary to use both of them

        Args:
        a - left part of the text
        b - round key

        Return: integer value"""
        return pow(a * b,
                   545735704168155525106215935941802819184685939157133628190496058664778626084654658157215100397614,
                   2 ** (self.blocksize // 2) - 1)

    def generate_round_keys(self) -> list:
        """This and other generate round keys functions is being used in the
        cipher. Functions don't take any arguments, although they use
        key and rounds count object's fields

        To generate round keys for every i, where i is round number,
        function takes 32 bits of the key starting from i. When function
        reaches the end of the key it continues from the beginning

        Return: list of integers"""
        round_keys = []
        bin_key = bin(self.key)[2:]
        for i in range(self.rounds_count):
            key = ""
            for j in range(32):
                key += bin_key[(i+j) % len(bin_key)]
            round_keys.append(int(key, 2))
        return round_keys

    def generate_round_keys_a(self) -> list:
        """This and other generate round keys functions is being used in the
        cipher. Functions don't take any arguments, although they use
        key and rounds count object's fields

        To generate round keys for every i, where i is round number,
        function takes 8 bits of the key startin from i. When function
        reaches the end it continues from the beginning.
        This 8 bits is used as initial value for LFSR with polynomial:
        00000011
        After that, function generate 32 bits for rounds keys with LFSR

        Return: list of integers"""
        round_keys = []
        polynom = [9, 1, 0]
        bin_key = bin(self.key)[2:]
        for i in range(self.rounds_count):
            root = ""
            for j in range(8):
                root += bin_key[(i + j) % len(bin_key)]
            root = int(root, 2)
            scrembler = LFSR.LFSR(polynom, root)
            bits = "".join(map(str, list(scrembler.get_bits(32))))
            round_keys.append(int(bits, 2))
        return round_keys

    def slice(self, text: bytes) -> list:
        """Slices given bytes to blocks with blocksize length. Function converts
        bytes to integer value, integer value to binary view and after that
        slices this binary into blocks of blocksize length.

        Args:
        text -- bytes of text

        Return: list of binary strings"""
        bin_text = bin(int.from_bytes(text, "big"))[2:]
        while len(bin_text) % self.blocksize != 0:
            bin_text = "0" + bin_text
        blocks = textwrap.wrap(bin_text, self.blocksize)
        return blocks

    def process(
                self, text: bytes,
                black_box: int = 1,
                decrypt: bool = False) -> bytes:
        """Processes given bytes with Feistel network algorithm.
        Function use slice() function to split bytes into the blocks. Then
        every block is being processed in the Feistel network
        Details of algorithm: https://en.wikipedia.org/wiki/Feistel_cipher
        After that, block are joined to one integer, this integer converts to
        bytes and returns.

        Args:
        text -- bytes of text to be processed
        black_box -- pointer to the function to use as black box.
            black_boxes:
                1: black_box_a(self, a, b)
                2: black_box_b(self, a, b)
                3: black_box(self, a, b)
            Warning! black_box_b still doesn't work properly
        decrypt -- defines the order of rounds keys.
            True: use rounds keys in reverse order
            False: use rounds keys in straight order

        Return: bytes of processed text.
        """
        blocks = self.slice(text)
        result_blocks = []
        part_length = self.blocksize // 2

        keys = self.round_keys
        if decrypt:
            keys.reverse()

        for block in blocks:

            left = int(block[:part_length], 2)
            right = int(block[part_length:], 2)

            for k in keys:
                t = left
                if black_box == 1:
                    f = self.black_box_a(left, k)
                elif black_box == 2:
                    f = self.black_box_b(left, k)
                else:
                    f = self.black_box(left, k)
                left = right ^ f
                right = t

            right, left = left, right

            left = bin(left)[2:]
            right = bin(right)[2:]
            while len(right) < part_length:
                right = "0" + right
            while len(left + right) < self.blocksize:
                left = "0" + left

            result_blocks.append(left + right)

        processed_text = "".join(result_blocks)
        processed_text = int(processed_text, 2)
        if decrypt:
            processed_text = processed_text.to_bytes(
                processed_text.bit_length(), "big").strip(b'\x00')
        else:
            processed_text = processed_text.to_bytes(
                processed_text.bit_length(), "big")

        return processed_text


def test():
    text = input("Enter text: ").encode()
    blocksize = int(input("Enter blocksize: "))
    print(f"Input text: {text}")
    cipher = Feistel(blocksize=blocksize, generation_method=2)
    enc_text = cipher.process(text)
    print(f"Encrypted text: {enc_text}")
    dec_text = cipher.process(enc_text, decrypt=True)
    print(f"Decrypted text: {dec_text.decode()}")


if __name__ == "__main__":
    test()
    input()


