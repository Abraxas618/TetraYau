# TetraCrypt Sovereign Benchmark Simulation Suite
# Tests: TKE, QIDL, RTH performance on your system

import time
import numpy as np
from hashlib import shake_256

# --- TKE MODULE ---
class TetrahedralKeyExchange:
    def __init__(self, seed=None):
        self.q = 8388607
        self.n = 4
        if seed:
            np.random.seed(seed)
        self.private_key = np.random.randint(0, self.q, self.n)
        self.public_matrix = self._generate_public_matrix()

    def _generate_public_matrix(self):
        base = np.array([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]])
        rotation = np.random.randint(1, 10)
        return np.mod(np.linalg.matrix_power(base, rotation), self.q)

    def generate_public_key(self):
        return np.dot(self.public_matrix, self.private_key) % self.q

    def compute_shared_secret(self, received_pubkey):
        return shake_256(np.dot(received_pubkey, self.private_key).tobytes()).digest(32)

# --- QIDL MODULE ---
def generate_isoca_dodecahedral_key(seed: int = 42):
    np.random.seed(seed)
    phi = (1 + np.sqrt(5)) / 2
    angles = np.linspace(0, 2 * np.pi, 20)
    key = np.array([np.cos(phi * angles), np.sin(phi * angles)]).T
    return key

def qidl_encrypt(message: str, key: np.ndarray, salt: str = "1234567890abcdef"):
    message += salt
    encoded = []
    for i, char in enumerate(message):
        char_val = ord(char)
        point = key[i % len(key)]
        transformed = (char_val * point[0], char_val * point[1])
        encoded.append(transformed)
    return encoded

# --- RTH MODULE ---
def recursive_tesseract_hash(data: bytes, depth: int = 4) -> bytes:
    h = data
    for i in range(depth):
        shake = shake_256()
        shake.update(h)
        h = shake.digest(64)
    return h

# --- BENCHMARK SUITE ---
def benchmark_tke(rounds=10000):
    start = time.time()
    for _ in range(rounds):
        alice = TetrahedralKeyExchange()
        bob = TetrahedralKeyExchange()
        alice_pub = alice.generate_public_key()
        bob_pub = bob.generate_public_key()
        alice_secret = alice.compute_shared_secret(bob_pub)
        bob_secret = bob.compute_shared_secret(alice_pub)
    end = time.time()
    return end - start

def benchmark_qidl(messages=5000):
    key = generate_isoca_dodecahedral_key()
    start = time.time()
    for i in range(messages):
        _ = qidl_encrypt(f"TetraQIDL_Message_{i}", key)
    end = time.time()
    return end - start

def benchmark_rth(recursions=100000):
    start = time.time()
    seed = b"TetraCrypt"
    for _ in range(recursions):
        _ = recursive_tesseract_hash(seed)
    end = time.time()
    return end - start

if __name__ == "__main__":
    print("\n[🔵] Stress Testing TKE (100,000 handshakes)...")
    tke_time = benchmark_tke(rounds=100_000)
    print(f"[TKE Stress] 100,000 Handshakes completed in {tke_time:.2f} seconds.")

    print("\n[🟢] Stress Testing QIDL (50,000 messages encrypted)...")
    qidl_time = benchmark_qidl(messages=50_000)
    print(f"[QIDL Stress] 50,000 Messages encrypted in {qidl_time:.2f} seconds.")

    print("\n[🟣] Stress Testing RTH (1,000,000 recursive hashes)...")
    rth_time = benchmark_rth(recursions=1_000_000)
    print(f"[RTH Stress] 1,000,000 Recursive Hashes completed in {rth_time:.2f} seconds.")

    print("\n🚀 Sovereign Stress Test Complete!")
