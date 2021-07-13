ogpass = ''
decrypted = b'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+'
encrypted = b'ph@#_%(9oib603$%+$%^&*e&m(2nkuygvcftjwaq751)-=4s8!'

scrambled = bytes.maketrans(decrypted, encrypted)
unscrambled = bytes.maketrans(encrypted, decrypted) 

print('''
> enter a 1 to encrypt
> enter a 2 to decrypt
> enter a 0 to quit
''')
input0 = input('> ')
while input != '0' :
    if input0 == '1':
        ogpass = input('''input password here
    > ''')

        print('here is your encrypted password')

        print(ogpass.translate(scrambled))

        break

    elif input0 == '2':
        ogpass = input('''input password here
    > ''')
        print('here is your decrypted password')
        print(ogpass.translate(unscrambled))
        break
    else:
        break




