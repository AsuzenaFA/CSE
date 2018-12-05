'''
def challenge1(first_name, last_name):
    print("So your name is %s, %s" % (last_name, first_name))


challenge1("Asuzena", "Flores")



def challenge2(numbers):

    number = int(input("Think of a number: "))
    mod = number % 2
    if mod > 0:
        print("Your number is odd.")
    else:
        print("Your number is even.")


challenge2(numbers)



def challenge3(base, height):
    b = int(input("Put in a base: "))
    h = int(input("Put in a height: "))
    area = b*h/2
    print("area = %d" % area)


challenge3(base, height)


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


def challenge7(integer):
    