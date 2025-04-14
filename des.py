import os
import sys
from des_utils import string_to_binary
from des_encryption import encrypt
from des_decryption import decrypt
from file_io import (
    read_text_file, write_text_file,
    save_encrypted_data, load_encrypted_data
)

def generate_key_from_password(password):
    """
    Generates a 64-bit key from a password.
    
    Args:
        password: Password string
        
    Returns:
        A 64-bit binary key
    """
    # Convert password to binary
    binary_password = string_to_binary(password)
    
    # Ensure key is exactly 64 bits by either truncating or padding
    if len(binary_password) >= 64:
        return binary_password[:64]
    else:
        return binary_password.ljust(64, '0')

def encrypt_file(input_file, output_file, password):
    """
    Encrypts the content of an input file and saves it to an output file.
    
    Args:
        input_file: Path to the input file
        output_file: Path to the output file
        password: Password for encryption
        
    Returns:
        True if successful, False otherwise
    """
    # Read input file
    plaintext = read_text_file(input_file)
    if plaintext is None:
        return False
    
    # Generate key from password
    key = generate_key_from_password(password)
    
    # Encrypt plaintext
    encrypted_data = encrypt(plaintext, key)
    
    # Save encrypted data
    return save_encrypted_data(output_file, encrypted_data)

def decrypt_file(input_file, output_file, password):
    """
    Decrypts the content of an input file and saves it to an output file.
    
    Args:
        input_file: Path to the input file
        output_file: Path to the output file
        password: Password for decryption
        
    Returns:
        True if successful, False otherwise
    """
    # Load encrypted data
    encrypted_data = load_encrypted_data(input_file)
    if encrypted_data is None:
        return False
    
    # Generate key from password
    key = generate_key_from_password(password)
    
    # Decrypt data
    decrypted_text = decrypt(encrypted_data, key)
    
    # Save decrypted text
    return write_text_file(output_file, decrypted_text)

def main():
    """
    Main function to handle command-line arguments and execute encryption/decryption.
    """
    if len(sys.argv) != 5:
        print("Usage: python des.py [encrypt|decrypt] [input_file] [output_file] [password]")
        return
    
    operation = sys.argv[1].lower()
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    password = sys.argv[4]
    
    if operation == "encrypt":
        if encrypt_file(input_file, output_file, password):
            print(f"File '{input_file}' encrypted successfully to '{output_file}'.")
        else:
            print("Encryption failed.")
    
    elif operation == "decrypt":
        if decrypt_file(input_file, output_file, password):
            print(f"File '{input_file}' decrypted successfully to '{output_file}'.")
        else:
            print("Decryption failed.")
    
    else:
        print("Invalid operation. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
