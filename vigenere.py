
def vigenere(text: str, key: str, t: int, mode: str) -> str:
    """
    Encrypt or decrypt text using Vigenere cipher.

    Parameters:
        text (str): Text to encrypt or decrypt
        key (str): Key to use for encryption or decryption
        t (str): Value of separator 
        mode (str): (e)ncrypt or (d)ecrypt

    Returns:
        str: Encrypted or decrypted text

    """
    # Make sure mode is 'e' or 'd'
    if mode not in ['e', 'd']:
        raise ValueError('Mode must be \'e\' or \'d\'')

    # Normalize text and key
    text = text.upper().replace(' ', '')
    key = key.upper().replace(' ', '')

    # Transform the mode to 1 or -1
    mode = 1 if mode == 'e' else -1

    # Iterate over text
    result = ''

    for i, letter in enumerate(text):
        # Get the key letter for the current position
        key_letter = key[i % len(key)]

        # Get the ord value of the resulting letter
        res_val = (ord(letter) + mode * ord(key_letter)) % 26 + ord('A')

        # Append the resulting letter to the result
        result += chr(res_val)

    # Add spaces every t characters
    result = ' '.join([result[i:i + t] for i in range(0, len(result), t)])
    return result
