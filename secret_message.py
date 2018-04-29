from Ciphers import Caesar, Affine, Atbash, Polybius

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
    cipher = raw_input(WELCOME_MESSAGE)
    try:
        cipher = CIPHERS[int(cipher)].name
    except ValueError:
        if not cipher.lower() in [c.name.lower() for c in CIPHERS.values()]:
            print('Can\'t find cipher with name {}. Restarting'.format(cipher))
            setup()
            return
    confirm = raw_input("Okay, so you chose {}, correct?\n".format(cipher))

    if not confirm.lower() in ['y', 'yes']:
        print('Okay, restarting')
        setup()
        return
    print('Cool! Let\'s get started!')


if __name__ == '__main__':
    setup()