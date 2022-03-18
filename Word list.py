import itertools

string = input('String to be permuted: ')

result = itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))
