import math
import random

from Prime import Prime


class RSA:
    def __init__(self,q,p):
        self.q = q
        self.p = p
        if not Prime.isPrime(q) or not Prime.isPrime(p):
            raise Exception("q and e must be prime numbers")
        self.n = q*p
        self.totientN = (q-1)*(p-1)
        self.e = RSA.generate_coprime(self.totientN)

        if math.gcd(self.e, self.totientN) != 1:
            raise ValueError("e and totientN are not coprime, choose a different e")

        self.d = pow(self.e, -1, self.totientN)
        print(f"encryption created your public keys are: n={self.n} e={self.e}")
        print(f"q={self.q} p={self.p}")
        print(f"the private key is {self.d}")

    def encrypt(self, m: int) -> int:
        return pow(m, self.e, self.n)

    def decrypt(self,c: int) -> int:
        return pow(c, self.d, self.n)

    @staticmethod
    def generate_coprime(number):
        while True:
            candidate = random.randint(2, number - 1)
            if math.gcd(candidate, number) == 1:
                return candidate
