from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

# Generate a random key and nonce
key = os.urandom(16)
nonce = os.urandom(16)

# Check that the key and nonce are 16 bytes
assert len(key) == 16, "Key length is not 16 bytes"
assert len(nonce) == 16, "Nonce length is not 16 bytes"

# Create the AES cipher in OFB mode
ctr = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))
aes = AES.new(key, AES.MODE_OFB, counter=ctr)

# Check that the counter value matches the nonce
assert ctr.nonce == nonce, "Nonce and counter nonce do not match"

# Generate 10 random numbers
for i in range(10):
    # Generate 128-bit random number
    rand_num = aes.encrypt(b'\x00' * 16)
    print(int.from_bytes(rand_num, byteorder='big'))
