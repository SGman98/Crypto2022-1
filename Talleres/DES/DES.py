# Receive an image in any format
import base64
from pyDes import des, CBC, PAD_PKCS5


def des_cbc(key):
    return des(key, CBC, b"00000000", padmode=PAD_PKCS5)


def encrypt(image_path, key):
    with open(image_path, 'rb') as image:  # rb = read binary
        image_bytes = image.read()
        image_bytes_des = des_cbc(key).encrypt(image_bytes)
        image_bytes_base64 = base64.b64encode(image_bytes_des)
        with open('encrypted.png', 'wb') as image:
            image.write(image_bytes_base64)
        return image_bytes_base64


def decrypt(encrypted_image, key):
    with open(encrypted_image, 'rb') as image:
        image_bytes_base64 = image.read()
        image_bytes = base64.b64decode(image_bytes_base64)
        image_bytes_des = des_cbc(key).decrypt(image_bytes)
        with open('decrypted.png', 'wb') as image:
            image.write(image_bytes_des)

        return image_bytes_des


def main():
    key = b'My 8 key'

    while True:
        encrypt_or_decrypt = input(
            'Enter (e)ncrypt (d)ecrypt (f)ull or (q)uit: ')

        if encrypt_or_decrypt not in ['e', 'encrypt', 'd', 'decrypt', 'f', 'full', 'q', 'quit']:
            print('Invalid input')
            return

        if encrypt_or_decrypt in ['q', 'quit']:
            return

        if encrypt_or_decrypt in ['e', 'encrypt', 'f', 'full']:
            image_path = input('Enter image path: ')
            encrypt_image = encrypt(image_path, key)
            print(f'Encrypted: {encrypt_image[:20]}...{encrypt_image[-20:]}')

        if encrypt_or_decrypt in ['d', 'decrypt', 'f', 'full']:
            image_path = input('Enter image path: ')
            decrypt_image = decrypt(image_path, key)
            print(f'Decrypted: {decrypt_image[:20]}...{decrypt_image[-20:]}')


if __name__ == '__main__':
    main()
