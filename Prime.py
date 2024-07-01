import math
import random
import time


class Prime:
    @staticmethod
    def isPrime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def find_random_coprime(n):
        while True:
            # Generate a random number m in the range from 2 to n-1
            m = random.randint(2, n - 1)
            # Check if m is co-prime with n
            if math.gcd(n, m) == 1:
                return m
    @staticmethod
    def primeBetween(startNum, endNum) -> list:
        startTime = time.time()
        primeList = []
        for i in range(startNum, endNum):
            if Prime.isPrime(i):
                primeList.append(i)
        endTime = time.time()
        print("finding all primes took:", endTime - startTime)
        return primeList

    @staticmethod
    def seceretCode(primeList):
        num1 = primeList.pop(random.randrange(len(primeList)))
        num2 = primeList.pop(random.randrange(len(primeList)))
        return num1 * num2

    @staticmethod
    def decode(key: int):
        if (Prime.isPrime(key)):
            print("no such code")
            return []
        for i in range(2, math.isqrt(key) + 1):
            if key % i == 0:
                j = key // i
                if Prime.isPrime(i) and Prime.isPrime(j):
                    return [i,j]
        return []

    @staticmethod
    def writePrimesToFile(start, end):
        filename = "primeFile.txt"
        newPrimes = Prime.primeBetween(start, end)
        try:
            with open(filename, "a") as primeFile:
                primeFile.write(f",{newPrimes}")
        except FileNotFoundError:
            with open(filename, 'w') as primeFile:
                primeFile.write(",".join(newPrimes))

    @staticmethod
    def generatePrime(length):
        baseNum = random.randint(pow(10, length - 1), pow(10, length) - 1)
        if baseNum % 2 == 0:
            baseNum += 1  # Make it odd to skip even numbers
        while True:
            if Prime.isPrime(baseNum):
                return baseNum
            baseNum += 2  # Increment by 2 to skip even numbers





