def is_even_or_odd(number):

    if (number % 2 == 0):
        print("Is Even")
    else:
        print("Is odd")


def is_even_or_odd_using_binary(number):
    binary = ""

    while (number > 0):
        binary = str(number/2) + binary
        number = number // 2

    if (binary[-1] == "0"):
        print("Is Even")
    else:
        print("Is odd")


is_even_or_odd(2)
is_even_or_odd_using_binary(2)
