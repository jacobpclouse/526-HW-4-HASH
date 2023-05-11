import hashlib

# SOURCE REFERENCED: https://nickthecrypt.medium.com/cryptography-hash-method-md2-message-digest-2-step-by-step-explanation-made-easy-with-python-10faa2e35e85
def divide_into_blocks(m):
    # Divide message into blocks of length 160 bits
    blocks = []
    block_size = 160
    num_blocks = len(m) // block_size
    for i in range(num_blocks):
        start = i * block_size
        end = (i+1) * block_size
        block = m[start:end]
        blocks.append(block)
    if len(m) % block_size != 0:
        # Add padding to the last block if necessary
        last_block = m[num_blocks*block_size:]
        last_block += b'\x00' * (block_size - len(last_block))
        blocks.append(last_block)
    return blocks


# SOURCE REFERENCED: https://realpython.com/python-zip-function/
def h2(blocks):
    num_blocks = len(blocks)
    blocksize = len(blocks[0])
    # hash block with block
    hash_result = ''
    # XOR the first block with the second block, and so on
    for i in range(1, num_blocks):
        # print(blocks[i-1])
        # print(blocks[i])
        for j in range(blocksize):
            output = blocks[i][j] ^ blocks[i-1][j]
            hash_result += str(output)
    
    return hash_result



# Example usage:
m = b'Ahe rain in spain falls neatly in the drain...The rain in spain falls neatly in the drain...The rain in spain falls neatly in the drain...The rain in spain fal1Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient.'
blocks = divide_into_blocks(m)
print(blocks)
hash_result = h2(blocks)
print(hash_result)

'''
One Way Property: This does satisfy the One Way Property. We divide a message  


Weak Collision Resistance: This is Weak Collision Resistant.


Strong Collision Resistance: This is Strong Collision Resistant. 

'''
