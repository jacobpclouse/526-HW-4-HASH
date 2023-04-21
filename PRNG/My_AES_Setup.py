import aes, os
key = os.urandom(16)
iv = os.urandom(16)

value = b'\x00' * 16
print(value)
# Generate 10 random numbers
for i in range(10):
    # Generate 128-bit random number
    # rand_num = aes.encrypt(b'\x00' * 16)
    encrypted = aes.AES(key).encrypt_ofb(value, iv)
    outNum = int.from_bytes(encrypted, byteorder='big')
    print(encrypted)
    print(outNum)
    newIv = int.from_bytes(iv,byteorder='big')
    # print(newIv)
    iv = (int.from_bytes(iv,byteorder='big') ^ outNum).to_bytes(16, byteorder='big')
    print(f"The new Iv will be: {iv}")




# encrypted = aes.AES(key).encrypt_ctr(b'Attack at dawn!!', iv)
# print(encrypted)
# print(aes.AES(key).decrypt_ctr(encrypted, iv))
# b'Attack at dawn'