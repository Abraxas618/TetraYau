# tke_example.py
# Example: Using Tetrahedral Key Exchange (TKE)

from tke import TetrahedralKeyExchange

def main():
    # Initialize two TKE participants
    alice = TetrahedralKeyExchange()
    bob = TetrahedralKeyExchange()

    # Each participant generates their public projection
    alice_pub = alice.generate_public()
    bob_pub = bob.generate_public()

    print("\nAlice's Public Matrix:")
    print(alice_pub)

    print("\nBob's Public Matrix:")
    print(bob_pub)

    # Exchange and derive shared secret keys
    alice_shared_key = alice.derive_shared_key(bob_pub)
    bob_shared_key = bob.derive_shared_key(alice_pub)

    print("\nAlice's Derived Shared Key:")
    print(alice_shared_key.hex())

    print("\nBob's Derived Shared Key:")
    print(bob_shared_key.hex())

    # Validate that both parties derived the same key
    if alice_shared_key == bob_shared_key:
        print("\n✅ Key Exchange Successful. Shared keys match.")
    else:
        print("\n❌ Key Exchange Failed. Shared keys do not match.")

if __name__ == "__main__":
    main()
