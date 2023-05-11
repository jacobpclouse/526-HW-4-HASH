from Crypto.Cipher import AES
import os
import binascii

def prng_aes_ofb(length):
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_OFB, iv)
    output = b''
    prev_block = iv
    for i in range(length):
        # Generate a 16-byte block of keystream
        keystream_block = cipher.encrypt(b'\x00' * 16)
        # XOR the keystream block with the previous block to produce the output
        output_block = bytes(a ^ b for a, b in zip(keystream_block, prev_block))
        output += output_block
        prev_block = keystream_block
    return output

def fraction_of_one_bits(data):
    num_ones = sum(bin(byte).count('1') for byte in data)
    return num_ones / (len(data) * 8)

def fraction_of_matching_bits(data):
    num_matches = 0
    for i in range(1, len(data)):
        prev_byte = data[i-1]
        curr_byte = data[i]
        # Count the number of matching bits in the two bytes
        num_matches += bin(prev_byte ^ curr_byte).count('0')
    return num_matches / (len(data) * 8)

# Test the PRNG by generating 10 random numbers
random_numbers = prng_aes_ofb(10)

# Print the random numbers in hexadecimal format
print("Random numbers:")
for num in random_numbers:
    print(binascii.hexlify(bytes([num])))

# Calculate the Fraction of One Bits and the Fraction of Matching Bits
print("Fraction of One Bits:", fraction_of_one_bits(random_numbers))
print("Fraction of Matching Bits:", fraction_of_matching_bits(random_numbers))
