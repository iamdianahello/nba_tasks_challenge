from sys import argv


def is_palindrome(num):
    num_array = [int(i) for i in str(num)]
    return num_array == list(reversed(num_array))


print(is_palindrome(argv[1]))
