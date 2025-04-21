
# 📜 VERIFY.md — TetraYau Sovereign Integrity Verification Guide

Welcome to the Sovereign Verification Protocol for **TetraYau v1.0**.

This guide ensures that any sovereign developer, cryptographer, or historian can verify the authenticity and integrity of the TetraYau archive.

Use IPFS Link or Orginal TetraYau-1.0.tar.gz to verify as .Zip changes hash
IPFS bafkreiasrqitizdcgxprnxsxqn74w3hqkprilhtndvzzd3qjb3nkvphzgq.gz
---

## 🛰 Prerequisites

- `openssl` installed (default on Linux/macOS, or install manually)
- `bash` terminal (Linux, macOS, WSL2 for Windows)
- Downloaded files:
  - `TetraYau-main.zip`
  - `checksums.txt`
  - `verify.sh` (this script)

---

## 🚀 Quick Verification Steps

### 1. Ensure all three files are in the same directory.

```bash
ls
TetraYau-main.zip  checksums.txt  verify.sh
```

### 2. Make the verification script executable.

```bash
chmod +x verify.sh
```

### 3. Run the Sovereign Verification Script.

```bash
./verify.sh
```

✅ If everything matches, you will see:

```
✅ Sovereign Verification Successful: Hashes Match!
```

❌ If there is a mismatch, the script will alert you immediately.

---

## 🌌 What This Verifies

- The archive `TetraYau-main.zip` is identical to the original Sovereign Genesis release.  
- No tampering, corruption, or unauthorized modification has occurred.  
- The integrity chain is anchored to Commander Michael Tass MacDonald (Abraxas618)'s Sovereign Genesis event (April 20–21, 2025).

---

## 📎 Manual Verification (Optional Advanced)

If you prefer to manually verify without using the script:

```bash
# Compute the local SHAKE256 hash manually
openssl dgst -shake256 -binary TetraYau-main.zip | xxd -p -c 256
```

Compare the output manually to the **Primary SHAKE256 (512-bit)** hash found inside `checksums.txt`.

---

## 🛡 Sovereignty Begins With Verification

Verifying integrity is the cornerstone of a sovereign civilization.

Thank you for participating in the Living Transmission.

Marsí.
