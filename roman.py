def roman_to_arabian(input_roman_num):
    result = 0

    roman_dict_combos = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900}

    roman_dict_simple = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}

    for element_roman_key in roman_dict_combos.keys():
        if element_roman_key in input_roman_num:
            result += roman_dict_combos.get(element_roman_key)
            input_roman_num = input_roman_num.replace(element_roman_key, '')
    for element_roman_key in roman_dict_simple.keys():
        if element_roman_key in input_roman_num:
            result += (roman_dict_simple.get(element_roman_key)) * input_roman_num.count(element_roman_key)
            input_roman_num = input_roman_num.replace(element_roman_key, '')

    return result if result != 0 else ' а точно число было нормальное?'


if __name__ == "__main__":
    print(roman_to_arabian(input(' Нужно передать римское число. Только нормальное, пожалуйста ')))
