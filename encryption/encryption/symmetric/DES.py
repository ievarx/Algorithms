# Tables for DES
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

PI = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

S = [
    [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ],
    [
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ],
    [
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ],
    [
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ],
    [
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ],
    [
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
    ],
    [
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
    ],
    [
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
    ]
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

iteration_shift = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

# Function to convert value to binary with padding
def to_binary(value, bits):
    return format(value, f'0{bits}b')

# Function to perform permutation
def permute(block, table, n):
    permutation = 0
    for i in range(len(table)):
        permutation <<= 1
        permutation |= (block >> (n - table[i])) & 0x01
    return permutation

# DES function with detailed round outputs
def des(input_block, key, mode):
    # Initial Permutation
    permuted_block = permute(input_block, IP, 64)
    print(f"After Initial Permutation (Hex): {permuted_block:016x}")
    print(f"After Initial Permutation (Binary): {to_binary(permuted_block, 64)}")
    
    L = (permuted_block >> 32) & 0xFFFFFFFF
    R = permuted_block & 0xFFFFFFFF
    
    # Key Schedule
    permuted_key = permute(key, PC1, 64)
    C = (permuted_key >> 28) & 0x0FFFFFFF
    D = permuted_key & 0x0FFFFFFF
    
    sub_keys = []
    for i in range(16):
        shift = iteration_shift[i]
        C = ((C << shift) | (C >> (28 - shift))) & 0x0FFFFFFF
        D = ((D << shift) | (D >> (28 - shift))) & 0x0FFFFFFF
        
        combined = (C << 28) | D
        sub_key = permute(combined, PC2, 56)
        sub_keys.append(sub_key)
    
    # 16 Rounds of Feistel Network
    for i in range(16):
        expanded_R = permute(R, E, 32)
        
        if mode == 'd':
            xor_result = expanded_R ^ sub_keys[15 - i]
        else:
            xor_result = expanded_R ^ sub_keys[i]
        
        s_box_output = 0
        for j in range(8):
            bits = (xor_result >> (42 - 6 * j)) & 0x3F
            row = ((bits & 0x20) >> 4) | (bits & 0x01)
            column = (bits >> 1) & 0x0F
            s_box_output <<= 4
            s_box_output |= S[j][16 * row + column]
        
        permuted_s_box_output = permute(s_box_output, P, 32)
        
        new_R = L ^ permuted_s_box_output
        L = R
        R = new_R
        
        # Print round outputs
        print(f"\nRound {i + 1}:")
        print(f"Subkey (Hex): {sub_keys[i]:012x}")
        print(f"Subkey (Binary): {to_binary(sub_keys[i], 48)}")
        print(f"L (Hex): {L:08x}")
        print(f"L (Binary): {to_binary(L, 32)}")
        print(f"R (Hex): {R:08x}")
        print(f"R (Binary): {to_binary(R, 32)}")
    
    final_block = (R << 32) | L
    output_block = permute(final_block, PI, 64)
    
    return output_block

# Function to convert text to 64-bit block
def text_to_64bit_block(text):
    byte_data = text.encode('utf-8')
    if len(byte_data) > 8:
        raise ValueError("Text must be 8 characters or less.")
    byte_data = byte_data.ljust(8, b'\x00')
    return int.from_bytes(byte_data, byteorder='big')

# Function to convert key to binary
def key_to_binary(key):
    byte_data = key.encode('utf-8')
    if len(byte_data) > 8:
        raise ValueError("Key must be 8 characters or less.")
    byte_data = byte_data.ljust(8, b'\x00')
    return int.from_bytes(byte_data, byteorder='big')

# Main function
def main():
    # Input text and key
    text = input("Enter text (up to 8 characters): ")
    key = input("Enter key (up to 8 characters): ")
    
    # Convert key to 64-bit block
    key_block = key_to_binary(key)
    
    # Convert text to 64-bit block
    input_block = text_to_64bit_block(text)
    
    # Encryption
    print("\n--- Encryption ---")
    encrypted = des(input_block, key_block, 'e')
    print(f"\nEncrypted (Hex): {encrypted:016x}")
    print(f"Encrypted (Binary): {to_binary(encrypted, 64)}")
    
    # Decryption
    print("\n--- Decryption ---")
    decrypted = des(encrypted, key_block, 'd')
    decrypted_text = decrypted.to_bytes(8, byteorder='big').decode('utf-8').rstrip('\x00')
    print(f"\nDecrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()