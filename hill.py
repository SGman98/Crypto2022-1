
def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of a and b.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of a and b.

    """
    while b != 0:
        a, b = b, a % b
    return a


def mod_inv(matrix: list, mod: int = 26) -> list:
    """
    Get the modular inverse of a matrix 2x2.

    Parameters:
        matrix (list): The matrix to get the inverse of.
        mod (int): The modulo.

    Returns:
        list: The inverse of the matrix.
    """
    inv_mat = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    # For each element of the matrix apply the modulo
    for row in inv_mat:
        for cell in row:
            cell %= mod

    return inv_mat


def hill(text: str, key: list, mode: str) -> str:
    """
    Encrypts or decrypts text using the Hill cipher.

    Parameters:
        text (str): The text to be encrypted or decrypted.
        key (list): A matrix 2x2 that represents the key.
        mode (str): (e)ncrypt or (d)ecrypt.

    Returns:
        str: The encrypted or decrypted text.

    """
    # Check if the key is a valid key
    assert len(key) == 2 and len(key[0]) == 2 and len(key[1]) == 2, \
        "The key must be a 2x2 matrix."

    det_key = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    # Check if the key is invertible and the determinant is coprime to 26
    assert det_key != 0 and gcd(det_key, 26) == 1, \
        "The key is not invertible or the determinant is not coprime to 26."

    # Check if the mode is valid
    assert mode in ["e", "d"], "The mode must be either 'e' or 'd'."

    # Normalize the text
    text = text.upper().replace(" ", "")

    # Get the modular inverse of the key if the mode is decrypts
    if mode == "d":
        key = mod_inv(key, 26)

    # for each pair of characters in the text get the ord mod 26
    letter_pairs_ord = []
    for l1, l2 in zip(text[::2], text[1::2]):
        letter_pairs_ord.append((ord(l1) - ord('A'), ord(l2) - ord('A')))

    # Get result ords
    result_ord = []
    for pair in letter_pairs_ord:
        result_ord.append(
            (pair[0] * key[0][0] + pair[1] * key[1][0]) % 26
        )
        result_ord.append(
            (pair[0] * key[0][1] + pair[1] * key[1][1]) % 26
        )

    # Convert the ords to letters
    return "".join([chr(i + ord('A')) for i in result_ord])
