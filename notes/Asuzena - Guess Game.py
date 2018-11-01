import random
a = (random.randint(1, 10))
guess = int(input("Guess a number form 1 to 10 "))
while a != "guess":
    print
    if guess < a:
        print("too low")
        guess = int(input("Guess a noumber for 1 to 10 "))
    elif 


