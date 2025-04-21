# qidl_example.py
# Example: Using Quantum Isoca-Dodecahedral Lattice Encryption (QIDL)

from qidl_encrypt import QuantumLatticeEncryptor

def main():
    # Initialize the Quantum Lattice Encryptor
    qidl = QuantumLatticeEncryptor()

    # Define a plaintext message
    plaintext = "The Sovereign Genesis Has Begun."

    print("\nOriginal Plaintext:")
    print(plaintext)

    # Encrypt the message
    ciphertext, salt = qidl.encrypt(plaintext)
    print("\nEncrypted Ciphertext:")
    print(ciphertext)
    print("\nEncryption Salt (for decryption):")
    print(salt)

    # Decrypt the message
    decrypted = qidl.decrypt(ciphertext, salt)
    print("\nDecrypted Plaintext:")
    print(decrypted)

    # Verify decryption correctness
    if plaintext == decrypted:
        print("\n✅ Decryption Successful. Integrity Verified.")
    else:
        print("\n❌ Decryption Failed. Mismatch Detected.")

if __name__ == "__main__":
    main()
