import hashlib

file1 = 'a.txt'
file2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'The file: {file1} is different from file: {file2}')
else:
    print(f'The file: {file1} is equall to file: {file2}')
