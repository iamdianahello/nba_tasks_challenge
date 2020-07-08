from sys import argv


def fibonacci(number):
    if number == 1:
        return [0]
    else:
        fibonacci_list = [0, 1]
        count = 2
        while count < number:
            fibonacci_list.append(fibonacci_list[count - 2] + fibonacci_list[count - 1])
            count += 1
        return fibonacci_list


if __name__ == "__main__":
    assert int(argv[1]) > 0, 'нам нужно число больше нуля, ну правда, ' + argv[1] + ' не прокатит'
    print(fibonacci(int(argv[1])))
