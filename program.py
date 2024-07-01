import random

from  RSA import  RSA
from  Prime import Prime
if __name__ == "__main__":
    primelist =Prime.primeBetween(100,200)
    q = primelist[random.randrange(len(primelist))]
    p = primelist[random.randrange(len(primelist))]
    encryption = RSA(q,primelist[random.randrange(len(primelist))],RSA.generate_coprime((q-1)*(p-1)))
    hiddenMessage = encryption.encrypt(32)
    print(f"encrypted message :{hiddenMessage}")
    decypheredMessage = encryption.decrypt(hiddenMessage)
    print(f"original message :{decypheredMessage}")