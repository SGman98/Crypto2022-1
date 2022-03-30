
def fix_text(text: str) -> str:
    """
    Fix the text implementing the playfair cipher rules.

    Remove spaces, replace j by i and remove spaces.
    If pairs of letters are the same, add an X in between.
    If length of the text is odd, add an X at the end.

    Parameters:
        text (str): Text to be fixed.

    Returns:
        str: Fixed text.

    """
    text = text.upper().replace('J', 'I').replace(' ', '')
    i = 0
    # Loop through the text
    while i < len(text):
        # If is the end of text and length is odd add X
        if i + 1 >= len(text):
            text += 'X'
            break
        # If the letters in the par is the same add X
        if text[i] == text[i + 1]:
            text = text[:i + 1] + 'X' + text[i + 1:]
        # Increment i by 2 to iterate through the pairs
        i += 2
    return text


def create_key(key: str) -> list:
    """
    Create a 5x5 matrix from a key.

    Parameters:
        key (str): Key to be used.

    Returns:
        list: Key matrix.

    """
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    # Fix the key, replacing j by i and removing spaces
    key = key.upper().replace('j', 'i').replace(' ', '')
    # Add the key to the start of the alphabet
    key += alphabet
    # Filter letters that are not in the alphabet
    key = ''.join(filter(lambda x: x in alphabet, key))
    # Remove duplicates and keep the order
    key = ''.join(dict.fromkeys(key))
    # Create the key matrix
    key = [key[i:i + 5] for i in range(0, len(key), 5)]
    return key


def find_pos(letter: str, key: list) -> tuple:
    """
    Find the position of a letter in the key matrix.

    Parameters:
        letter (str): Letter to be found.
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
    # Fix the text
    text = fix_text(text)
    # Create the key matrix
    key = create_key(key)
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
    return result
