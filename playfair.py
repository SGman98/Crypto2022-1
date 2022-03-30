
def normalize(text: str) -> str:
    """
    Normalize the text implementing the rules of the playfair cipher.

    Remove spaces, replace j by i and remove spaces.
    If pairs of letters are the same, add an X in between.
    If length of the text is odd, add an X at the end.

    Parameters:
        text (str): Raw text.

    Returns:
        str: Normalized text.

    """
    # Upper case, replace j by i and remove spaces
    text = text.upper().replace('J', 'I').replace(' ', '')

    i = 0
    # Loop through the text in pairs
    while i < len(text) - 1:
        # If the letters in the par are the same, add an X
        if text[i] == text[i + 1]:
            text = text[:i + 1] + 'X' + text[i + 1:]

        i += 2

    # If the length of the text is odd, add an X at the end
    if len(text) % 2 == 1:
        text += 'X'

    return text


def gen_matrix(key: str) -> list:
    """
    Create a 5x5 matrix from a key.

    Parameters:
        key (str): Key to be used.

    Returns:
        list: Key matrix.

    """
    # English alphabet without j
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    # Fix the key replacing j by i
    key = key.upper().replace('J', 'I')

    # Add the key and the alphabet in one string
    key += alphabet

    # Filter letters in the key that are not in the alphabet
    key = ''.join(filter(lambda x: x in alphabet, key))

    # Remove duplicates keeping the order of the letters
    key = ''.join(dict.fromkeys(key))

    # Create the key matrix
    key = [key[i:i + 5] for i in range(0, len(key), 5)]
    return key


def find_pos(letter: str, key: list) -> tuple:
    """
    Find the position of a letter in the key matrix.

    Parameters:
        letter (str): Letter that we want to find.
        key (list): Key matrix.

    Returns:
        tuple: Row and column of the letter.

    """
    # Transform the key to a string
    key = ''.join(key)

    # Find the position of the letter in the key
    row = key.find(letter) // 5
    col = key.find(letter) % 5
    return row, col


def playfair(text: str, key: str, mode: str) -> str:
    """
    Encrypt or decrypt a text using the playfair cipher.

    Parameters:
        text (str): Text to be encrypted or decrypted.
        key (str): Key to be used.
        mode (str): (e)ncrypt or (d)ecrypt.

    Returns:
        str: Encrypted or decrypted text.

    """
    # Make sure mode is 'e' or 'd'
    if mode not in ['e', 'd']:
        raise ValueError('Mode must be \'e\' or \'d\'')

    # Normalize the text with the rules of the playfair cipher
    text = normalize(text)

    # Convert the key to a matrix
    key = gen_matrix(key)

    # Transform the mode to 1 or -1
    mode = 1 if mode == 'e' else -1

    result = ''

    # Loop through the text in pairs
    for l1, l2 in zip(text[::2], text[1::2]):
        # Find the position of each letter
        row1, col1 = find_pos(l1, key)  # First letter
        row2, col2 = find_pos(l2, key)  # Second letter

        # If the letters are in the same row
        if row1 == row2:
            result += key[row1][(col1 + mode) % 5]
            result += key[row2][(col2 + mode) % 5]
            continue

        # If the letters are in the same column
        if col1 == col2:
            result += key[(row1 + mode) % 5][col1]
            result += key[(row2 + mode) % 5][col2]
            continue

        # If the letters are in different rows and columns
        result += key[row1][col2]
        result += key[row2][col1]

    # Add spaces between the pairs
    result = ' '.join(result[i:i + 2] for i in range(0, len(result), 2))
    return result
