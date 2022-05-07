# Receive an image in any format
import base64
import os
from pyDes import des, CBC, PAD_PKCS5


def des_cbc(key):
    return des(key, CBC, b"00000000", padmode=PAD_PKCS5)


def img_name(image_path):
    path, name = os.path.split(image_path)
    name, ext = os.path.splitext(name)
    name = name.replace('_encrypted', '').replace('_decrypted', '')
    return path, name, ext


def encrypt(image_path, key):
    path, name, ext = img_name(image_path)
    with open(image_path, 'rb') as img:
        image_bytes = img.read()
        image_bytes_des = des_cbc(key).encrypt(image_bytes)
        image_bytes_base64 = base64.b64encode(image_bytes_des)

        enc_path = os.path.join(path, f'{name}_encrypted{ext}')
        with open(enc_path, 'wb') as enc_img:
            enc_img.write(image_bytes_base64)
        return image_bytes_base64, enc_path


def decrypt(encrypted_image, key):
    path, name, ext = img_name(encrypted_image)

    with open(encrypted_image, 'rb') as img:
        image_bytes_base64 = img.read()
        image_bytes = base64.b64decode(image_bytes_base64)
        image_bytes_des = des_cbc(key).decrypt(image_bytes)

        dec_path = os.path.join(path, f'{name}_decrypted{ext}')
        with open(dec_path, 'wb') as dec_img:
            dec_img.write(image_bytes_des)

        return image_bytes_des, dec_path


def main():
    while True:
        encrypt_or_decrypt = input(
            '\nEnter (e)ncrypt (d)ecrypt (f)ull or (q)uit: ')

        if encrypt_or_decrypt not in ['e', 'encrypt', 'd', 'decrypt', 'f', 'full', 'q', 'quit']:
            print('Invalid input')
            continue

        if encrypt_or_decrypt in ['q', 'quit']:
            return

        image_path = input('Enter image path: ')
        key = input('Enter key 8 characters (12345678): ')
        key = bytes(key or '12345678', 'utf-8')

        if encrypt_or_decrypt in ['e', 'encrypt', 'f', 'full']:
            print('Encrypting...')
            encrypt_image, image_path = encrypt(image_path, key)
            print(f'Encrypted: {encrypt_image[:20]}...{encrypt_image[-20:]}')
            print(f'Saved to: {image_path}\n')

        if encrypt_or_decrypt in ['d', 'decrypt', 'f', 'full']:
            print('Decrypting...')
            decrypt_image, image_path = decrypt(image_path, key)
            print(f'Decrypted: {decrypt_image[:20]}...{decrypt_image[-20:]}')
            print(f'Saved to: {image_path}\n')


if __name__ == '__main__':
    main()
