import random
n = random.randint(0, 10)
win = False
guessesTaken = 0
guess = int(input("I am thinking of a number between 1 and 10 "))
guessesTaken = guessesTaken + 1
while n != guess and not win and guessesTaken < 5:
    if guess < n:
        print("too low")
        guess = int(input("Guess again "))
    elif guess > n:
        print("too high")
        guess = int(input("Guess again"))
    elif guess == n:
        print("You are correct")
        win = True
    elif guessesTaken > 5:
        win = False