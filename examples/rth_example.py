# rth_example.py
# Example: Using Recursive Tesseract Hashing (RTH)

from rth import RecursiveTesseractHasher

def main():
    # Initialize the Recursive Tesseract Hasher
    rth = RecursiveTesseractHasher()

    # Define input data
    input_data = "Initialize Sovereign Identity"

    print("\nOriginal Input Data:")
    print(input_data)

    # Generate the recursive hash
    hash_output = rth.hash(input_data)

    print("\nRecursive Tesseract Hash Output:")
    print(hash_output)

    # Rehash to verify consistency (hash of hash)
    rehashed_output = rth.hash(hash_output)

    print("\nRecursive Re-Hash (Evolutionary Step):")
    print(rehashed_output)

if __name__ == "__main__":
    main()
