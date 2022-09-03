def convert_integer_to_roman(num):
    num_and_sym = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
        5000: "V(-)",
        10000: "X(-)",
        50000: "L(-)",
        100000: "C(-)",
        500000: "D(-)",
        1000000: "M(-)",
    }
    index = len(num_and_sym) - 1
    result = ""

    while num > 0:
        div = num // list(num_and_sym.keys())[index]
        num %= list(num_and_sym.keys())[index]

        while div > 0:
            result += list(num_and_sym.values())[index]
            div -= 1
        index -= 1

    return result
