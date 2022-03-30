
def caesar(text: str, k: int, mode: str) -> str:
    """
    Encrypt or decrypt a text using the Caesar cipher.

    Parameters:
        text (str): Text to be encrypted or decrypted.
        k (int): Number of shifts.
        mode (str): (e)ncrypt or (d)ecrypt.

    Returns:
        str: Encrypted or decrypted text.

    """
    # Get the alphabet
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Make sure mode is 'e' or 'd'
    if mode not in ['e', 'd']:
        raise ValueError('Mode must be \'e\' or \'d\'')

    # Normalize the text to uppercase and remove spaces
    text = text.upper().replace(' ', '')

    # Tranform the mode to 1 or -1
    mode = 1 if mode == 'e' else -1

    result = ''

    for letter in text:
        if letter in a:
            # Shift the letter by k
            shift_index = (a.index(letter) + k * mode) % len(a)
            result += a[shift_index]

    # Add spaces every 5 characters
    result = ' '.join(result[i:i + 5] for i in range(0, len(result), 5))
    return result
