import os
import sys

from Ciphers import Affine, Atbash, Caesar, Polybius

### Initial startup message
WELCOME_MESSAGE = '''
Hi there!

Welcome to the MrLotU Encryption tool!

To start, please choose a chiper from the list below:
    1. Caesar
    2. Affine
    3. Atbash
    4. Polybius

Either give the name or the number associated.
'''

### List of ciphers that the program can use
CIPHERS = {
    1: Caesar,
    2: Affine,
    3: Atbash,
    4: Polybius
}

def setup():
    """Setup function, sets up the encryption tool for use"""
    ### Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    ### Get the desired cipher
    cipher = input(WELCOME_MESSAGE)
    try:
        ### Get cipher if we got a number as input
        cipher = CIPHERS[int(cipher)]
    except ValueError:
        ### Create list of cipher names
        cipher_names = [c.name.lower() for c in CIPHERS.values()]
        ### Check if the input is the name of one of our ciphers
        if not cipher.lower() in cipher_names:
            ### If not, restart the setup
            print('Can\'t find cipher with name {}. Restarting'.format(cipher))
            setup()
            return
        else:
            ### Set the cipher if we got a name as input
            cipher = cipher_names[cipher_names.index(cipher.lower())]

    ### Confirm the cipher we selected
    confirm = input('Okay, so you chose {}, correct? \033[4mY\033[0m/n\t'.format(cipher.name))

    if not confirm.lower() in ['y', 'yes', '']:
        print('Okay, restarting')
        setup()
        return
    print('Cool! Let\'s get started!')
           
    ### Ask if we want to use a time pad
    pad = input('Would you like to use a one time pad to add an extra layer of security? \033[4mY\033[0m/n\t')

    if not pad.lower() in ['y', 'yes', '']:
        print('Okay, not using pad!')
        pad_value = None
    else:
        ### Instantiate the one time pad
        pad_value = input('Please give me a string to use as one time pad\t')

    ### Setup the cipher for use
    cipher.setup(encrypt, decrypt, input, pad_value)

def encrypt(cipher):
    """
    Encrypt function

    Params
        ------
        cipher : `Cipher`
            The cipher to use for encryption.
    """
    msg = input('Okay! Please give me a message to encrypt\t')
    output = cipher.encrypt(msg)
    print('Your encrypted message is: {}'.format(output))
    finalize()

def decrypt(cipher):
    """
    Decrypt function

    Params
        ------
        cipher : `Cipher`
            The cipher to use for decryption.
    """
    msg = input('Okay! Please give me a message to decrypt\t')
    output = cipher.decrypt(msg)
    print('Your decrypted message is: {}'.format(output))
    finalize()

def finalize():
    """Function called to either restart the session or finalize it"""
    close = input('Would you like to encrypt/decrypt something else? \033[4mY\033[0m/n\t')

    if close.lower() in ['y', 'yes', '']:
        print('Okay, restarting!')
        setup()
    else:
        print('Okay! We hope to see you again!')

if __name__ == '__main__':
    ### Fix for using python 2
    try: input = raw_input
    except NameError: pass
    ### Clean exit
    try:
        setup()
    except KeyboardInterrupt:
        print('\nWe hope to see you again!')
        sys.exit(0)
