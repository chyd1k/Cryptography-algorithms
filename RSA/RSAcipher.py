import math
import textwrap
import crypto_numbers


class RSA:
    """This class implements RSA encryption algorithm. It provides methods for
    generation public and private keys, for export and import this keys and
    for encryption and decryption text.
    """
    def __init__(self, prime_sizes: int = 2048):
        """Object constructor

        Args:
            prime_sizes -- this argument defines bit length of prime numbers p
                and q, that will be generated during key generation method.
        """
        self.size = prime_sizes
        self.public_key = ()
        self.private_key = ()
        self.block_size = 0

    def slice(self, text: int) -> list:
        """Slices given integer into blocks of bit with size equals block_size

        Args:
            text -- integer value

        Return: list of binary strings"""
        bin_text = bin(text)[2:]
        while len(bin_text) % self.block_size != 0:
            bin_text = "0" + bin_text
        blocks = textwrap.wrap(bin_text, self.block_size)
        return blocks

    def join(self, blocks: list) -> int:
        """This method joins integers into one. Each integer is being converted
        into bit string, bit string then completed with 0 to the block_size bit
        length. Then all strings are being joined and converted back to integer

        Args:
            blocks -- list of integers to be joined

        Return: integer value
        """
        blocks = [bin(block)[2:] for block in blocks]
        result = blocks[0]
        for i in range(1, len(blocks)):
            while len(blocks[i]) < self.block_size:
                blocks[i] = "0" + blocks[i]
            result += blocks[i]
        result = int(result, 2)
        return result

    def encrypt(self, text) -> int:
        """This function encrypts text. Before calling this method keys must be
        set.

        Args:
             text -- integer value or bytes to be encrypted

        Return: integer value
        """
        if type(text) != int and type(text) != bytes:
            raise TypeError(f"Text must be {bytes} or {int}")
        if type(text) == bytes:
            text = int.from_bytes(text, "big")
        text = self.slice(text)
        for i in range(len(text)):
            block = int(text[i], 2)
            block = pow(block, self.public_key[0], self.public_key[1])
            text[i] = block
        text = self.join(text)
        return text

    def decrypt(self, text) -> int:
        """This function decrypts text. Before calling this method keys must be
        set.

        Args:
            text -- bytes or integer value to be decrypted

        Result: integer value
        """
        if type(text) != int and type(text) != bytes:
            raise TypeError(f"Text must be {bytes} or {int}")
        if type(text) == bytes:
            text = int.from_bytes(text, "big")
        text = self.slice(text)
        for i in range(len(text)):
            block = int(text[i], 2)
            text[i] = pow(block, self.private_key[0], self.private_key[1])
        text = self.join(text)
        return text

    def generate_keys(self, p: int = None,
                      q: int = None, e: int = None):
        """This method generates public and private keys.

        Args:
             p, q -- prime numbers
             e -- public exponent
             All three arguments should be given or none of them
        """
        if not p or not q or not e:
            p = crypto_numbers.get_prime(self.size)
            q = crypto_numbers.get_prime(self.size)
            e = 65537
        else:
            if not crypto_numbers.is_prime(p, 10):
                raise ValueError("Given p is not prime number")
            if not crypto_numbers.is_prime(q, 10):
                raise ValueError("Given q is not prime number")
            if p == q:
                raise ValueError("p and q shouldn't be equal")
            if e == p or e == q or e >= (p - 1) * (q - 1) or e <= 1:
                raise ValueError("Wrong e value")
        n = p * q
        self.block_size = round(math.log2(n))
        phi = (p - 1) * (q - 1)
        res = crypto_numbers.gcd(e, phi)
        while res["reminder"] != 1:
            e += 1
            res = crypto_numbers.gcd(e, phi)
        d = res["x"] % phi
        self.public_key = (e, n)
        self.private_key = (d, n)

    def export_keys(self, public: str = None, private: str = None):
        """This function writes public and private keys to files.

        Args:
             public -- name of file to write public key in
             private -- name of file to write private key in
        """
        if not public:
            public = "PUBLIC.key"
        public_key = f"{self.public_key[0]}\n{self.public_key[1]}".encode()
        with open(public, "wb") as f:
            f.write(public_key)
        if not private:
            private = "PRIVATE.enc"
        private_key = f"{self.private_key[0]}\n{self.private_key[1]}".encode()
        with open(private, "wb") as f:
            f.write(private_key)

    def import_keys(self, public: str = None, private: str = None):
        """This method sets public and private keys from files.

        Args:
             public -- name of file where public key is stored
             private -- name of file where private key is stored
        """
        if public:
            with open(public, "rb") as f:
                self.public_key = tuple(map(int, f.read().decode().splitlines()))
            self.block_size = round(math.log2(self.public_key[1]))
        if private:
            with open(private, "rb") as f:
                self.private_key = tuple(map(int, f.read().decode().splitlines()))
            self.block_size = round(math.log2(self.private_key[1]))


if __name__ == "__main__":
    inp = input("Enter text to test encryption and decryption: ").encode()
    cipher = RSA(prime_sizes=512)
    cipher.generate_keys()
    print(f"Plain text: {inp}")
    enc_text = cipher.encrypt(inp)
    print(f"Encrypted text: {enc_text}")
    dec_text = cipher.decrypt(enc_text)
    print(f"Decrypted text: {dec_text}")
    dec_text = dec_text.to_bytes(dec_text.bit_length(), "big")
    print(f"Decrypted text: {dec_text.decode()}")
