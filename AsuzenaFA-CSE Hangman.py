
import random
word_bank = ["pink dolphin", "spongebob", "aurthor", "princess peach", "mario", "bambi", "stitch", "pepa pig",
             "bowser", "potato head", ]
a = word_bank

string1 = (random.choice(word_bank))
list1 = list(string1)
print("-".replace(string1))
print(" ".join(string1))

win = False
guesses_left = 8
guess = int(input("take a guess "))
guesses_left = guesses_left - 1
while guesses_left > 0 and not win:
    guesses_left -= 1
    if guess > string1 in a:
        guess = input("Guess again")
    elif guess < string1 in a:
        guess = input("Guess again")
    elif guess == string1 in a:
        input("You guessed right take another guess ")
    elif guesses_left <= 0:
        win = False
        print("You are out of guesses you lose")
