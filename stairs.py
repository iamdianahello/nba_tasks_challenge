from sys import argv

i = 1
while i <= int(argv[1]):
    print(' ' * (int(argv[1]) - i) + '#' * i)
    i = i + 1
