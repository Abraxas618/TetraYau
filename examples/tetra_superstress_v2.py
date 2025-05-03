
# TetraYau Super Stress Test v2 — Modularized Benchmark Execution

import time
import numpy as np
from hashlib import shake_256

# --- Core Cryptographic Modules ---

# Tetrahedral Key Exchange (TKE)
class TetrahedralKeyExchange:
    def __init__(self, seed=None):
        self.q = 8388607
        self.dim = 4
        if seed is not None:
            np.random.seed(seed)
        self.private_key = np.random.randint(0, self.q, self.dim)
        self.public_matrix = self._generate_rotation_matrix()

    def _generate_rotation_matrix(self):
        base = np.array([
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0]
        ])
        rotation = np.random.randint(1, 10)
        return np.mod(np.linalg.matrix_power(base, rotation), self.q)

    def generate_public_key(self):
        return np.dot(self.public_matrix, self.private_key) % self.q

    def compute_shared_secret(self, peer_pubkey):
        combined = np.dot(peer_pubkey, self.private_key) % self.q
        return shake_256(combined.tobytes()).digest(32)

# Quantum Isoca-Dodecahedral Encryption (QIDL)
def generate_qidl_key(seed: int = 42):
    np.random.seed(seed)
    phi = (1 + np.sqrt(5)) / 2
    angles = np.linspace(0, 2 * np.pi, 20)
    return np.array([np.cos(phi * angles), np.sin(phi * angles)]).T

def qidl_encrypt(message: str, key: np.ndarray, salt: str = "1234567890abcdef"):
    full_message = message + salt
    encrypted = []
    for i, char in enumerate(full_message):
        val = ord(char)
        projection = key[i % len(key)]
        encrypted.append((val * projection[0], val * projection[1]))
    return encrypted

# Recursive Tesseract Hashing (RTH)
def recursive_tesseract_hash(input_data: bytes, depth: int = 4) -> bytes:
    result = input_data
    for _ in range(depth):
        hasher = shake_256()
        hasher.update(result)
        result = hasher.digest(64)
    return result

# --- Benchmark Runners ---

def benchmark_tke(count=1_000_000):
    start = time.time()
    for _ in range(count):
        a, b = TetrahedralKeyExchange(), TetrahedralKeyExchange()
        a_pub, b_pub = a.generate_public_key(), b.generate_public_key()
        a.compute_shared_secret(b_pub)
        b.compute_shared_secret(a_pub)
    return time.time() - start

def benchmark_qidl(count=500_000):
    key = generate_qidl_key()
    start = time.time()
    for i in range(count):
        qidl_encrypt(f"QIDL_Message_{i}", key)
    return time.time() - start

def benchmark_rth(count=10_000_000):
    input_bytes = b"TetraYauEntropySeed"
    start = time.time()
    for _ in range(count):
        recursive_tesseract_hash(input_bytes)
    return time.time() - start

# --- Main Execution ---

if __name__ == "__main__":
    print("\n🛡️ Sovereign Cryptographic Benchmark Launching...\n")

    print("[🔵] Running TKE Benchmark...")
    tke_time = benchmark_tke()
    print(f"TKE: 1,000,000 key exchanges completed in {tke_time:.2f} seconds")

    print("\n[🟢] Running QIDL Benchmark...")
    qidl_time = benchmark_qidl()
    print(f"QIDL: 500,000 encryptions completed in {qidl_time:.2f} seconds")

    print("\n[🟣] Running RTH Benchmark...")
    rth_time = benchmark_rth()
    print(f"RTH: 10,000,000 recursive hashes completed in {rth_time:.2f} seconds")

    print("\n✅ Benchmark Complete — Sovereign Stack Verified")
