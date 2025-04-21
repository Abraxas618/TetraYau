# hbb_example.py
# Example: Using Hypercube-Based Blockchain (HBB)

from hbb_blockchain import HyperBlock, HypercubeBlockchain
import time

def main():
    # Initialize the Hypercube Blockchain
    chain = HypercubeBlockchain()

    # Create some dummy data blocks
    block_data = [
        "Initialize Sovereign Genesis",
        "Record Sovereign Key Exchange Event",
        "Secure Morphogenetic Ledger",
        "Encrypted Communications Established",
        "TetraYau Operational Launch"
    ]

    # Add blocks to the blockchain
    for data in block_data:
        print(f"\nAdding block with data: {data}")
        chain.add_block(data)
        time.sleep(0.5)  # simulate passage of time

    # Validate the blockchain
    is_valid = chain.is_valid()
    print("\nBlockchain validity check:", "✅ VALID" if is_valid else "❌ INVALID")

    # Display the blockchain
    print("\n--- Full Hypercube Blockchain ---")
    for block in chain.chain:
        print(f"\nBlock Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Tesseract Hash: {block.tesseract_hash}")

if __name__ == "__main__":
    main()
