'''
def challenge1(first_name, last_name):
    print("So your name is %s, %s" % (last_name, first_name))


challenge1("Asuzena", "Flores")


def challenge2(number):

    number = int(input("Think of a number: "))
    mod = number % 2
    if mod > 0:
        print("Your number is odd.")
    else:
        print("Your number is even.")


challenge2(int)


def challenge3(base, height):
    b = int(input("Put in a base: "))
    h = int(input("Put in a height: "))
    area = b*h/2
    print("area = %d" % area)


challenge3(input, input)


def challenge4(number):

    number = int(input("Type a negative or a positive number: "))
    if number < 0:
        print("This is a negative.")
    elif number > 0:
        print("THis is a positive.")


challenge4(4)


def challenge5(radius):
    area = 3.14 * radius**2

    print("area = %s" % area)


challenge5(2.4)


def challenge6(radius):
    volume = 4/3 * 3.14 * radius**3
    print("volume = %s" % volume)


challenge6(2.4)
'''


def challenge9(letter):
    vowel_list = ["a", "o", "u", "e", "i"]
    letter_list = ["b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q",
                   "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter = int(input("Type in a vowel or andy other letter: "))
    if letter == vowel_list:
        print("This is a vowel.")
    elif letter == letter_list:
        print("This is NOT a vowel.")


challenge9(int)
