
from des_utils import PC1, PC2, SHIFT_TABLE, permute, left_shift

def generate_subkeys(key):
    """
    Generates 16 subkeys from the main key.
    
    Args:
        key: A 64-bit key as a binary string
        
    Returns:
        A list of 16 subkeys, each 48 bits long
    """
    # Apply PC1 permutation to get a 56-bit key
    key = permute(key, PC1)
    
    # Split the key into left and right halves (28 bits each)
    left = key[:28]
    right = key[28:]
    
    subkeys = []
    
    # Generate 16 subkeys
    for i in range(16):
        # Perform left shifts according to shift table
        left = left_shift(left, SHIFT_TABLE[i])
        right = left_shift(right, SHIFT_TABLE[i])
        
        # Combine left and right halves
        combined = left + right
        
        # Apply PC2 permutation to get a 48-bit subkey
        subkey = permute(combined, PC2)
        subkeys.append(subkey)
    
    return subkeys
