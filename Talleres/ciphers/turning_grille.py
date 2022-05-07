# turning grille cipher

def turning_grille(text: str, key: str, direction: str, mode: str):
    """
    Encrypt or decrypt text using turning grille cipher.

    Parameters:
        text (str): Text to be encrypted or decrypted
        key (str):
            key to be used use 'O' for a hole in the grid and '.' for empty space
            to separate rows use ',' or '|', or ' ' or '\n'
        direction (str): (l)eft or (r)ight
        mode (str): (e)ncrypt or (d)ecrypt

    Returns:
        str: encrypted/decrypted text

    """
    # remove , or |, or breaklines or spaces
    key = key.replace(',', '').replace('|', '').replace('\n', '').replace(' ', '')
    # key only contains O and .
    assert all([char in 'O.' for char in key]), 'key must only contain O and .'
    size = len(key) ** 0.5
    assert size == (size := int(size)), 'key must be a square matrix'
    assert mode in ['e', 'd'], "mode must be 'e' or 'd'"
    assert direction in ['l', 'r'], "direction must be 'l' or 'r'"

    # normalize text
    text = text.upper().replace(' ', '')
    assert text.isalpha(), "text must be a string of letters"

    # transform key into a list of coordinates
    key_list = []
    for i in range(size):
        for j in range(size):
            if key[i * size + j] == 'O':
                key_list.append((i, j))

    rot_coords = [key_list.copy()]
    for _ in range(3):
        rot = []
        # for the last coords, rotate them
        for x, y in rot_coords[-1]:
            if direction == 'l':
                rot.append((abs(y - (size - 1)), x))
            else:
                rot.append((y, abs(x - (size - 1))))
        rot_coords.append(rot)


    tmp_rot = sum(rot_coords, [])
    rep_ = [x for x in set(tmp_rot) if tmp_rot.count(x) > 1]
    if len(rep_) == 1:
        tx, ty = rep_[0]
        if size % 2 == 1:
            assert tx == size // 2 and ty == size // 2, 'there is a repeated coord'
            for rot in rot_coords[1:]:
                rot.remove((tx, ty))
    else:
        assert len(rep_) == 0, 'there are repeated coords'


    # sort the coords for each rotation by x and y
    rot_coords = [sorted(rot) for rot in rot_coords]

    if mode == 'e':
        # create a list since strings are immutable
        result = ['.'] * size * size
        for rot in rot_coords:
            for x, y in rot:
                result[x * size + y] = text[0]
                text = text[1:]
        result = ''.join(result)
    else:
        result = ''
        for rot in rot_coords:
            for x, y in rot:
                result += text[x * size + y]

    return ' '.join(result[i:i + size] for i in range(0, len(result), size))


print(turning_grille('jim attacks at dawn', 'O...|....|.O.O|..O.', 'l', 'e'))
print(turning_grille('jktd saat wiam cnat', 'O...|....|.O.O|..O.', 'l', 'd'))
text = 'TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I'
key = """
O..O.O...
..O.....O
.O....O..
..O.O..O.
....O.O.O
...O...O.
O....O...
.O..O...O
..O......"""
print(turning_grille(text, key, 'l', 'd'))