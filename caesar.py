
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
    assert mode in ['e', 'd'], "Mode must be 'e' or 'd'"
    # k must be an integer
    assert isinstance(k, int), "k must be an integer"

    # Normalize the text to uppercase and remove spaces
    text = text.upper().replace(' ', '')
    assert text.isalpha(), "Text must contain only letters"

    # Get the alphabet
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
