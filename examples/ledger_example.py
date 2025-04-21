# ledger_example.py
# Example: Using the Sovereign Ledger

from ledger import SovereignLedger
import time

def main():
    # Initialize the Sovereign Ledger
    ledger = SovereignLedger()

    # Create some dummy ledger events
    events = [
        "Genesis: Sovereign Initialization",
        "TKE: Secure Key Exchange with Node 42",
        "RTH: Identity Hash Anchor Updated",
        "QIDL: Encrypted Message Transmission",
        "Deployment: Sovereign Node Network Expansion"
    ]

    # Add events to the ledger
    for event in events:
        print(f"\nRecording Event: {event}")
        ledger.record(event)
        time.sleep(0.5)  # simulate passage of time

    # Display the full ledger
    print("\n--- Full Sovereign Ledger ---")
    for i, entry in enumerate(ledger.entries):
        print(f"\nEntry #{i}")
        print(f"Node ID: {entry['node_id']}")
        print(f"Data: {entry['data']}")
        print(f"Phase-State Hash: {entry['phase_state_hash']}")
        print(f"Timestamp: {entry['timestamp']}")

    # Display the latest sovereign state hash
    print("\n--- Current Sovereign Ledger Hash ---")
    print(ledger.last_hash())

if __name__ == "__main__":
    main()
