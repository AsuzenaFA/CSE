import random
guess_left = 5
number = (random.randint(1, 10))
win = False
guess = int(input("Guess a number between 1 and 10"))
while guess_left > 0 and not win:
    print("i am thinking of a number between 1 and 10")
    print("take a guess ")

    guess_left -= 1
    if guess == number:
     print("correct you guess it")
     win = False
    else:
        if number > guess:
            print("to low")
        elif number < guess:
            print("to high")
     if guess_left == 0:
         print("ran out of guesses")
         win = True