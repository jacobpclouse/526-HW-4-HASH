'''
HM4 - ICSI 526 Cryptography - JACOB CLOUSE
           ______  _____            _____  _____  _   _  _____ 
     /\   |  ____|/ ____|          |  __ \|  __ \| \ | |/ ____|
    /  \  | |__  | (___    ______  | |__) | |__) |  \| | |  __ 
   / /\ \ |  __|  \___ \  |______| |  ___/|  _  /| . ` | | |_ |
  / ____ \| |____ ____) |          | |    | | \ \| |\  | |__| |
 /_/    \_\______|_____/           |_|    |_|  \_\_| \_|\_____|                                                     
(using OFB mode)
'''

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from Crypto.Cipher import AES
import os
import binascii

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function to generate the random values with AES OFB ---
# SOURCE: https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
def prng_aes_ofb(length):
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_OFB, iv)
    output = b''
    prev_block = iv
    for i in range(length):
        # Generate a 16-byte block 
        keystream_block = cipher.encrypt(b'\x00' * 16)
        # XOR the keystream block with the previous block to produce the output
        output_block = bytes(a ^ b for a, b in zip(keystream_block, prev_block))
        output += output_block
        prev_block = keystream_block
    return output

# --- Function to find fraction of one bits ---
def fraction_of_one_bits(data):
    num_ones = sum(bin(byte).count('1') for byte in data)
    return num_ones / (len(data) * 8)

# --- Function to find matching bits ---
def fraction_of_matching_bits(data):
    num_matches = 0
    for i in range(1, len(data)):
        prev_byte = data[i-1]
        curr_byte = data[i]
        # Count the number of matching bits
        num_matches += bin(prev_byte ^ curr_byte).count('0')
    return num_matches / (len(data) * 8)

# --- Function to print out my Logo ---
def myLogo():
    print("Created and Tested by: ")
    print("   __                  _         ___ _                       ")
    print("   \ \  __ _  ___ ___ | |__     / __\ | ___  _   _ ___  ___  ")
    print("    \ \/ _` |/ __/ _ \| '_ \   / /  | |/ _ \| | | / __|/ _ \ ")
    print(" /\_/ / (_| | (_| (_) | |_) | / /___| | (_) | |_| \__ \  __/ ")
    print(" \___/ \__,_|\___\___/|_.__/  \____/|_|\___/ \__,_|___/\___| ")
    print("Dedicated to Peter Zlomek and Harely Alderson III")


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

myLogo()

# Generating 10 random numbers
random_numbers = prng_aes_ofb(10)

# Print the random numbers 
print("Random numbers:")
for num in random_numbers:
    print(binascii.hexlify(bytes([num])))

# Calculate the Fraction of One Bits & Fraction of Matching Bits
print("Fraction of One Bits:", fraction_of_one_bits(random_numbers))
print("Fraction of Matching Bits:", fraction_of_matching_bits(random_numbers))
