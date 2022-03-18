import hashlib
import sys

start = 0

while start == 0:

    string = input('Text here: ')

    menu = (input('''$$$$ Menu - Chose the hash type $$$$
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                
                Type the number of the corresponded hash: '''))

    if not menu.isnumeric():
        print('Error! Type a number, please!')
        continue
    menu = int(menu)

    if menu == 1:
        result = hashlib.md5(string.encode('utf-8'))
        print('The MD5 hash of the string ', string, 'is: ', result.hexdigest())
        sys.exit()
    elif menu == 2:
        result = hashlib.sha256(string.encode('utf-8'))
        print('The SHA1 hash of the string ', string, 'is: ', result.hexdigest())
        sys.exit()
    if menu == 3:
        result = hashlib.sha256(string.encode('utf-8'))
        print('The SHA256 hash of the string ', string, 'is: ', result.hexdigest())t
        sys.exit()
    elif menu == 4:
        result = hashlib.sha512(string.encode('utf-8'))
        print('The SHA512 hash of the string ', string, 'is: ', result.hexdigest())
        sys.exit()
    else:
        print('Something is wrong, choose a number for 1 to 4, please')
        continue







