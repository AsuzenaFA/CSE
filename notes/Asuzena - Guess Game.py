import random
a = (random.randint(1, 10))
guess = int(input("Guess a number form 1 to 10 "))
while a != "guess":
    for i in range(5):
        if guess < a:
            print("too low")
            guess = int(input("Guess a noumber for 1 to 10 "))
        elif guess > a:
            print("too high")
            guess = int(input("guess a noumber form 1 to 10 "))
        elif a == guess:
            for i in {1}:
                print("correct")
