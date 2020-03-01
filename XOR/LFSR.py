from typing import Iterable, Generator


class LFSR:
    """This class implements LFSR and function to generate random bits with it
    """
    def __init__(self, polynom: Iterable[int], root: int = None):
        """Object's constructor

        Args:
            polynom -- equations coeffitioents to make a scrembler
            root -- initial scrembler value
        """
        # First, I make the list from Iterable, and sort this list from
        # max value to min
        polynom = list(polynom)
        polynom.sort(reverse=True)

        # Next, I check given polynomial
        # If it contains only zeroes or it there is only 1 value in it
        # I raise a ValueError
        if set(polynom[1:]) == {0} or polynom[1:] == []:
            raise ValueError("Given wrong polynomial")

        # Also each object in the list must be positive integer
        for i in polynom:
            if i < 0:
                raise ValueError("Polynomial can't contain negatives")
            if type(i) != int:
                raise TypeError("Polynomial can contain only integer values")

        # If everything is okay with the list I cut first value from it
        # and save it
        # Also I save the size of my lfsr as highest value in polynom + 1
        self.polynom = polynom[1:]
        self.size = polynom[0]

        # If root wasn't given, I generate random one
        if not root:
            import time
            root = int(round(time.time() * 1000)) % (2 ** self.size + 1)

        # Next, I check the type of the root (if it passed)
        if type(root) != int:
            raise TypeError(f"Root must be integer, not {type(root)}")

        # Finally, I save root value and the lfsr is ready
        self.root = root % (2 ** self.size)

    def get_bits(self, count: int) -> Generator:
        """This function generates some bits using lfsr
        count - this argument defines how much bits to be generated

        Args:
            count -- count of bits to be generated

        Return: returns generator
        """
        for i in range(count):
            yield self.root & 0x01
            shifts = []
            for power in self.polynom:
                if power == 0:
                    shifts.append(self.root)
                else:
                    shifts.append(self.root >> power)

            xors = shifts.pop(0)
            while len(shifts) != 0:
                xors ^= shifts.pop(0)

            xors = xors & 0x01
            xors = xors << self.polynom[0]

            self.root = xors | (self.root >> 1)


def main():
    p = list(map(int, input(
        "Enter polynomial powers (integers separated by space): ").split(" ")))
    try:
        r = int(input("Enter initial scrembler value: "))
    except Exception:
        r = None

    c = int(input("How much bits to generate: "))
    scr = LFSR(p, r)
    print(f'''Your Scrembler:
        Polynomial: {" ".join(map(str, scr.polynom))}
        Root: {scr.root}
        Size: {scr.size}
        ''')
    sequence = list(scr.get_bits(c))
    print(f"Sequence: {' '.join(map(str, sequence))}")


if __name__ == "__main__":
    main()
