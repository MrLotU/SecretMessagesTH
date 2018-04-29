import os

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
    cipher = raw_input(WELCOME_MESSAGE)
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
    confirm = raw_input('Okay, so you chose {}, correct? \033[4mY\033[0m/n\t'.format(cipher.name))

    if not confirm.lower() in ['y', 'yes', '']:
        print('Okay, restarting')
        setup()
        return
    print('Cool! Let\'s get started!')

    cipher.setup(encrypt, decrypt)

def encrypt(cipher):
    msg = raw_input('Okay! Please give me a message to encrypt\t')
    output = cipher.encrypt(msg)
    print('Your encrypted message is: {}'.format(output))
    finalize()

def decrypt(cipher):
    msg = raw_input('Okay! Please give me a message to decrypt\t')
    output = cipher.decrypt(msg)
    print('Your decrypted message is: {}'.format(output))
    finalize()

def finalize():
    close = raw_input('Would you like to encrypt/decrypt something else? \033[4mY\033[0m/n\t')

    if close.lower() in ['y', 'yes', '']:
        print('Okay, restarting!')
        setup()
    print('Okay! We hope to see you again!')
    return

if __name__ == '__main__':
    setup()
