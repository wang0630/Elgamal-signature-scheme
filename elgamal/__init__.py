import os
import random
from cryptography.hazmat.primitives import hashes


class Elgamal:
    def __init__(self, msg):
        self.alpha = None
        self.gamma = None
        self.k = None
        self.delta = None
        # Convert msg to byte
        self.msg = msg.encode()

        # Hash-then-sign
        self.digest = hashes.Hash(hashes.SHA256())
        self.digest.update(self.msg)
        self.hs = self.digest.finalize()
        self.hs_int = int.from_bytes(self.hs, byteorder='big')

        # Generate prime number
        p = int.from_bytes(os.urandom(256), byteorder="big")
        print('Getting a big prime number....')

        while not self.is_prime(p):
            p = int.from_bytes(os.urandom(256), byteorder="big")

        self.p = p
        print(f'Big prime is {p}')
        # Generate private key
        self.private = random.randint(1, self.p - 1)

    def sign(self):
        print('Signing....')
        self.alpha = random.randint(1, self.p - 1)

        # Make sure gcd(k, self.p-1) = 1
        self.k = random.randint(1, self.p - 2)
        while self.gcd(self.p - 1, self.k) != 1:
            self.k = random.randint(1, self.p - 2)

        self.gamma = pow(self.alpha, self.k, self.p)
        # Calculate k^-1
        k_inv = pow(self.k, -1, self.p - 1)
        tmp = (self.hs_int - self.gamma * self.private) * k_inv
        self.delta = tmp % (self.p - 1)
        print('Signing finished....')

    def verify(self):
        print('Verifying....')
        # beta is the public key
        beta = pow(self.alpha, self.private, self.p)
        print(f'public key is {beta}')
        return (pow(beta, self.gamma, self.p)*pow(self.gamma, self.delta, self.p)) % self.p == pow(self.alpha, self.hs_int, self.p)

    # Primality test with Fermat's little Theorem
    def is_prime(self, p):
        if p == 1:
            return False
        if p == 2:
            return True

        if p % 2 == 0:
            return False

        # Try five times
        for _ in range(5):
            elm = random.randint(2, p-1)
            if pow(elm, p - 1, p) != 1:
                print(f'fail {p}')
                return False

        return True

    # gcd with Euclidean algorithm
    def gcd(self, a, b):
        while a % b != 0:
            tmp = a
            a = b
            b = tmp % b

        return b
