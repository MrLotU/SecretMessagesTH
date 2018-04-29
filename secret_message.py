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
    1: 'Caesar',
    2: 'Affine',
    3: 'Atbash',
    4: 'Polybius'
}

def setup():
    cipher = raw_input(WELCOME_MESSAGE)
    if int(cipher) != None:
        cipher = CIPHERS[int(cipher)]
    confirm = raw_input("Okay, so you chose {}, correct?\n".format(cipher))

    if not confirm.lower() in ['y', 'yes']:
        print('Okay, restarting')
        setup()
        return
    print('Cool! Let\'s get started!')

if __name__ == '__main__':
    setup()