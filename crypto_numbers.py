"""This module contains some useful functions to work with numbers.
This functions are usually used in cryptography.
There is a list of all functions in this module:
"""

import random


def gcd(a: int, b: int) -> dict:
    """Extended Euklid algorithm. Finds greatest common divisor of a and b

    Args:
        a -- first number
        b -- second number

    Return: dictionary with specified keys:
        reminder -- greatest common divisor
        x, y -- answers to equation ax + by = reminder
    """
    if b == 0:
        return {"x": 1, "y": 0, "reminder": a}
    else:
        answer = gcd(b, a % b)
        x = answer["x"]
        y = answer["y"]
        d = answer["reminder"]
        ret = {"reminder": d, "x": y, "y": x - a // b * y}
        return ret


def is_prime(p: int, t: int) -> bool:
    """Miller-Rabin primality test. Error probability is (1/4)^t
    More about Miller-Rabin test:
    https://en.wikipedia.org/wiki/Miller–Rabin_primality_test

    Args:
        p -- number to be tested
        t -- count of tests

    Return: True if the number is prime, else - False
    """
    if p <= 0:
        return False
    if p == 2 or p == 1:
        return True
    temp = p - 1
    b = 0
    while temp % 2 == 0:
        temp = temp // 2
        b += 1
    m = (p - 1) // 2 ** b
    for i in range(t):
        a = random.randint(2, p-1)
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


def get_prime(n: int) -> int:
    """Function generates random prime number with bit length equals n

    Args:
        n -- bit length of generated number

    Return: prime number
    """
    while True:

        # Here I use random.getrandbits to generate n random bits
        # Although higher bits might be 0, so actually this number may have
        # bit length less then n.
        # Moreover, lowest bit might be 0, so this number is not prime
        # To fix this I switch lowest bit to 1, and after that, while
        # the bit length of number less than n I complete it with 1 and 0.
        # For example, n = 4, but generated 0010, so it's 2. And actual bit
        # length is 2 (10). So I do this:
        # 1) Switch lowest bit to 1 and I get number 3 -> 11
        # 2) Complete number to 4 bits, so that highest bit is 1: 11 -> 1011
        if n <= 1:
            return
        bits = list(bin(random.getrandbits(n))[2:])
        bits[-1] = "1"
        while len(bits) < n:
            bits.insert(0, "0")
        bits[0] = "1"
        num = int("".join(bits), 2)

        # Now I has actual n bits number, but I cant say it's prime
        # So I check it
        # First, I check if the number is divisible by any of prime numbers
        # from 2 to 200
        little_primes = [
            2, 3, 5, 7, 11, 13, 17, 19,
            23, 29, 31, 37, 41, 43, 47,
            53, 59, 61, 67, 71, 73, 79,
            83, 89, 97, 101, 103, 107,
            109, 113, 127, 131, 139, 149,
            151, 157, 163, 167, 173, 179,
            181, 191, 193, 197, 199
        ]
        little_checks = [num % p == 0 and num != p for p in little_primes]
        if True in little_checks:
            continue

        # If it's not, I run Miller-Rabin test 10 times for this number
        # If number passes the test I return it. And it's prime with the
        # probability of 0.9999990463256836
        if is_prime(num, 10):
            return num


def prime_factors(n: int) -> list:
    """Function finds all prime divisors of the given number

    Args:
        n -- number to be factorized

    Return: list of factors
    """
    if is_prime(n, 10):
        return [n]

    import math
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    sq_root = round(math.sqrt(n))
    for i in range(3, sq_root, 2):
        while n % i == 0:
            n = n // i
            factors.append(i)
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return factors


def euler_func(n: int) -> int:
    """Function counts the positive integers up to a given integer n that are
    relatively prime to n. More about Euler's function:
    https://en.wikipedia.org/wiki/Euler%27s_totient_function

    Args:
        n -- number to be processed

    Return: result of the Euler's function work
    """
    if is_prime(n, 10):
        return n - 1
    n_factors = set(prime_factors(n))
    result = n
    for i in n_factors:
        result *= (1 - 1/i)
    return round(result)


def primitive_root(n: int, phi_factors: list = None) -> int:
    """Function finds primitive root modulo n

    Args:
        n -- modulo

    Return: integer which is primitive root or None if nothing found
    """
    phi = euler_func(n)
    if not phi_factors:
        phi_factors = prime_factors(phi)
    for g in range(2, n + 1):
        check = True
        for p in phi_factors:
            check &= pow(g, phi // p, n) != 1
        if check:
            return g


def get_dh_nums(length: int) -> tuple:
    q = get_prime(length-1)
    p = 2
    n = p * q + 1
    while not is_prime(n, 10) or n.bit_length() != length:
        q = get_prime(length-1)
        n = p * q + 1
    g = primitive_root(n, [p, q])
    return n, g


def shift(lst, count):
    """Does cycle shift of the subscriptable object to n positions

    Args:
        lst -- object to be shifted
        count -- count of positions the lst to be shifted

    Return: shifted object
    """
    return lst[count:] + lst[:count]
