# Receive an image in any format
import base64
from pyDes import des, CBC, PAD_PKCS5


def des_cbc(key):
    return des(key, CBC, b"00000000", padmode=PAD_PKCS5)


def img_name(image_path):
    image_path = image_path.split('/')[-1]
    name, ext = image_path.split('.')
    name = name.replace('_encrypted', '').replace('_decrypted', '')
    return name, ext


def encrypt(image_path, key):
    name, ext = img_name(image_path)
    with open(image_path, 'rb') as image:  # rb = read binary
        image_bytes = image.read()
        image_bytes_des = des_cbc(key).encrypt(image_bytes)
        image_bytes_base64 = base64.b64encode(image_bytes_des)

        image_new_path = f'{name}_encrypted.{ext}'
        with open(image_new_path, 'wb') as img_enc:
            img_enc.write(image_bytes_base64)
        return image_bytes_base64, image_new_path


def decrypt(encrypted_image, key):
    name, ext = img_name(encrypted_image)
    with open(encrypted_image, 'rb') as image:
        image_bytes_base64 = image.read()
        image_bytes = base64.b64decode(image_bytes_base64)
        image_bytes_des = des_cbc(key).decrypt(image_bytes)

        image_new_path = f'{name}_decrypted.{ext}'
        with open(image_new_path, 'wb') as img_dec:
            img_dec.write(image_bytes_des)

        return image_bytes_des, image_new_path


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

        image_path = input('Enter image path: ')

        if encrypt_or_decrypt in ['e', 'encrypt', 'f', 'full']:
            encrypt_image, image_path = encrypt(image_path, key)
            print(f'Encrypted: {encrypt_image[:20]}...{encrypt_image[-20:]}')
            print(f'Saved to: {image_path}')

        if encrypt_or_decrypt in ['d', 'decrypt', 'f', 'full']:
            decrypt_image, image_path = decrypt(image_path, key)
            print(f'Decrypted: {decrypt_image[:20]}...{decrypt_image[-20:]}')
            print(f'Saved to: {image_path}')


if __name__ == '__main__':
    main()
