import time
from RSA import RSA
from Prime import Prime

if __name__ == "__main__":
    enc = RSA(5645926316268074971, 6167827644893731781)

    start_time = time.time()

    message = "hello this is a hidden message"

    encrypted_values = []

    # Encrypt the message
    for char in message:
        encrypted_value = enc.encrypt(ord(char))
        encrypted_values.append(encrypted_value)

    decrypted_message = ""

    # Decrypt the message
    for encrypted_value in encrypted_values:
        decrypted_value = enc.decrypt(encrypted_value)
        decrypted_message += chr(decrypted_value)

    print(f"Decrypted Message: {decrypted_message}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time / 60} minutes")
