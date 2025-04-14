
import os
import binascii

def read_text_file(filename):
    """
    Reads text from a file.
    
    Args:
        filename: Path to the input file
        
    Returns:
        Text content of the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None

def write_text_file(filename, content):
    """
    Writes text to a file.
    
    Args:
        filename: Path to the output file
        content: Text content to write
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")
        return False

def write_binary_file(filename, content):
    """
    Writes binary content to a file.
    
    Args:
        filename: Path to the output file
        content: Binary content to write
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filename, 'wb') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")
        return False

def read_binary_file(filename):
    """
    Reads binary content from a file.
    
    Args:
        filename: Path to the input file
        
    Returns:
        Binary content of the file
    """
    try:
        with open(filename, 'rb') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None

def save_encrypted_data(filename, encrypted_data):
    """
    Saves encrypted data to a file in hex format for readability.
    
    Args:
        filename: Path to the output file
        encrypted_data: Encrypted binary data
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Convert binary data to hexadecimal representation
        hex_data = binascii.hexlify(encrypted_data.encode()).decode()
        
        with open(filename, 'w') as file:
            file.write(hex_data)
        return True
    except Exception as e:
        print(f"Error saving encrypted data to {filename}: {e}")
        return False

def load_encrypted_data(filename):
    """
    Loads encrypted data from a file in hex format.
    
    Args:
        filename: Path to the input file
        
    Returns:
        Decrypted binary data
    """
    try:
        with open(filename, 'r') as file:
            hex_data = file.read().strip()
        
        # Convert hexadecimal back to binary data
        binary_data = binascii.unhexlify(hex_data).decode()
        return binary_data
    except Exception as e:
        print(f"Error loading encrypted data from {filename}: {e}")
        return None
