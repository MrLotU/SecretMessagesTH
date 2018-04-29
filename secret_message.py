import os
import sys

from Ciphers import Affine, Atbash, Caesar, Polybius

WELCOME_MESSAGE = '''
Hi there!

Welcome to the MrLotU Encryption tool!

To start, please choose a chiper from the list below:
    1. Caesar
    2. Affine
    3. Atbash
    4. Polybius
'''

CIPHERS = {
    1: Caesar,
    2: Affine,
    3: Atbash,
    4: Polybius
}

def setup():
    os.system('cls' if os.name == 'nt' else 'clear')
    cipher = input(WELCOME_MESSAGE)
    try:
        cipher = CIPHERS[int(cipher)]
    except ValueError:
        cipher_names = [c.name.lower() for c in CIPHERS.values()]
        if not cipher.lower() in cipher_names:
            print('Can\'t find cipher with name {}. Restarting'.format(cipher))
            setup()
            return
        else:
            cipher = cipher_names[cipher_names.index(cipher.lower())]
    confirm = input('Okay, so you chose {}, correct? \033[4mY\033[0m/n\t'.format(cipher.name))

    if not confirm.lower() in ['y', 'yes', '']:
        print('Okay, restarting')
        setup()
        return
    print('Cool! Let\'s get started!')

    cipher.setup(encrypt, decrypt)

def encrypt(cipher):
    msg = input('Okay! Please give me a message to encrypt\t')
    output = cipher.encrypt(msg)
    print('Your encrypted message is: {}'.format(output))
    finalize()

def decrypt(cipher):
    msg = input('Okay! Please give me a message to decrypt\t')
    output = cipher.decrypt(msg)
    print('Your decrypted message is: {}'.format(output))
    finalize()

def finalize():
    close = input('Would you like to encrypt/decrypt something else? \033[4mY\033[0m/n\t')

    if close.lower() in ['y', 'yes', '']:
        print('Okay, restarting!')
        setup()
    else:
        print('Okay! We hope to see you again!')

if __name__ == '__main__':
    try: input = input
    except NameError: pass
    setup()
