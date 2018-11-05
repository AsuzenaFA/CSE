import random
number = (random.randint(1, 10))
guess = + 1
guess_taken = guess
print("I am thinking of a number between 1 and 10")
print(input(" take a guess "))
while guess_taken < 5:
    if guess < number:
        print("too low, guess higher")
    if guess > number:
        print("too high, guess lower")








