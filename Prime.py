import math
import random
import time


class Prime:
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

    def primeBetween(startNum, endNum) -> list:
        startTime = time.time()
        primeList = []
        for i in range(startNum, endNum):
            if Prime.isPrime(i):
                primeList.append(i)
        endTime = time.time()
        print("finding all primes took:", endTime - startTime)
        return primeList

    def seceretCode(primeList):
        num1 = primeList.pop(random.randrange(len(primeList)))
        num2 = primeList.pop(random.randrange(len(primeList)))
        return num1 * num2

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

    def writePrimesToFile(start, end):
        filename = "primeFile.txt"
        newPrimes = Prime.primeBetween(start, end)
        try:
            with open(filename, "a") as primeFile:
                primeFile.write(f",{newPrimes}")
        except FileNotFoundError:
            with open(filename, 'w') as primeFile:
                primeFile.write(",".join(newPrimes))





