from des_utils import (
    IP, FP, E, P, S_BOX, permute, xor,
    string_to_binary, binary_to_string, pad_text
)
from des_key import generate_subkeys

def encrypt_block(block, subkeys):
    """
    Encrypts a 64-bit block using DES algorithm.
    
    Args:
        block: A 64-bit binary string
        subkeys: List of 16 subkeys generated from the main key
        
    Returns:
        A 64-bit encrypted binary string
    """
    # Initial Permutation
    block = permute(block, IP)
    
    # Split the block into left and right halves (32 bits each)
    left = block[:32]
    right = block[32:]
    
    # 16 rounds of encryption
    for i in range(16):
        # Expand right half from 32 to 48 bits
        right_expanded = permute(right, E)
        
        # XOR with the current round subkey
        xor_result = xor(right_expanded, subkeys[i])
        
        # S-box substitution (48 bits -> 32 bits)
        s_box_output = apply_sbox(xor_result)
        
        # Permutation
        permuted = permute(s_box_output, P)
        
        # XOR with left half
        new_right = xor(left, permuted)
        
        # Swap left and right for next round
        left = right
        right = new_right
    
    # Combine right and left (note the swap for the final combination)
    combined = right + left
    
    # Final Permutation
    ciphertext = permute(combined, FP)
    
    return ciphertext

def apply_sbox(bits):
    """
    Applies S-box substitution to convert 48 bits to 32 bits.
    
    Args:
        bits: A 48-bit binary string
        
    Returns:
        A 32-bit binary string after S-box substitution
    """
    output = ""
    
    # Process 6 bits at a time through 8 S-boxes
    for i in range(8):
        # Extract 6 bits for current S-box
        chunk = bits[i*6:(i+1)*6]
        
        # First and last bits determine row (0-3)
        row = int(chunk[0] + chunk[5], 2)
        
        # Middle 4 bits determine column (0-15)
        col = int(chunk[1:5], 2)
        
        # Get value from S-box table and convert to 4-bit binary
        val = S_BOX[i][row][col]
        output += format(val, '04b')
    
    return output

def encrypt(plaintext, key):
    """
    Encrypts plaintext using DES algorithm.
    
    Args:
        plaintext: String to encrypt
        key: 64-bit key as a binary string
        
    Returns:
        Encrypted text as a binary string
    """
    # Pad plaintext to ensure it's a multiple of 8 bytes
    padded_text = pad_text(plaintext)
    
    # Generate subkeys
    subkeys = generate_subkeys(key)
    
    # Convert padded text to binary
    binary_text = string_to_binary(padded_text)
    
    # Process each 64-bit block
    encrypted_binary = ""
    for i in range(0, len(binary_text), 64):
        block = binary_text[i:i+64]
        encrypted_block = encrypt_block(block, subkeys)
        encrypted_binary += encrypted_block
    
    # Convert binary to string (this will be in binary format)
    encrypted_text = binary_to_string(encrypted_binary)
    
    return encrypted_text
