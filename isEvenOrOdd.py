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

# OLD CODE


def is_even_or_odd_using_binary2(number):
    tamanho = [0, 0, 0, 0]

    for i in range(number):
        for m in tamanho:
            if (m == 0):
                tamanho[m] = 1
            elif (m > 1):
                tamanho[m] = 0
                tamanho[m+1] = 1
            else:
                tamanho[m] = 0

    print(tamanho)

# NEW CODE


def is_even_or_odd_using_binary3(number):
    mylist = [0]
    size = len(mylist)
    cont = 0

    if (number == 1):
        mylist[0] = 1
        return False

    for i in range(number):
        for m in range(len(mylist)):
            if (mylist[m] == 0):
                mylist[m] = 1
                cont = cont+1
            elif (mylist[m] == 1 and mylist[0] == 1):
                mylist[m] = 0
                cont = cont+1
                if (cont == number):
                    mylist.append(1)

    mylist.reverse
    for i in mylist:
        print(mylist)
    if (mylist[size-1] == 0):
        return True
    else:
        return False


is_even_or_odd(3)
is_even_or_odd_using_binary(3)
is_even_or_odd_using_binary2(3)
is_even_or_odd_using_binary3(3)
