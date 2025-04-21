
#!/bin/bash

# TetraYau Sovereign Genesis Verification Script
# Version: 1.0

ARCHIVE="TetraYau-main.zip"
CHECKSUM_FILE="checksums.txt"

echo "🔍 Verifying TetraYau Sovereign Archive Integrity..."

# Check if both files exist
if [[ ! -f "$ARCHIVE" ]]; then
  echo "❌ Archive file $ARCHIVE not found!"
  exit 1
fi

if [[ ! -f "$CHECKSUM_FILE" ]]; then
  echo "❌ Checksum file $CHECKSUM_FILE not found!"
  exit 1
fi

# Extract expected SHAKE256 hash from checksums.txt
EXPECTED_HASH=$(grep -A1 "Primary SHAKE256" "$CHECKSUM_FILE" | tail -n1 | tr -d ' ')

# Generate SHAKE256 (512-bit) hash of the archive
echo "🔧 Computing local SHAKE256 (512-bit) hash..."
LOCAL_HASH=$(openssl dgst -shake256 -binary "$ARCHIVE" | xxd -p -c 256)

# Compare hashes
echo "🔎 Expected Hash:"
echo "$EXPECTED_HASH"
echo "🔎 Computed Hash:"
echo "$LOCAL_HASH"

if [[ "$EXPECTED_HASH" == "$LOCAL_HASH" ]]; then
  echo "✅ Sovereign Verification Successful: Hashes Match!"
  exit 0
else
  echo "❌ Verification Failed: Hash Mismatch!"
  exit 2
fi
