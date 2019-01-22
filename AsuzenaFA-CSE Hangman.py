
import string
import random
word_bank = ["pink dolphin", "Spongebob", "Aurthor", "Princess Peach", "Mario", "Bambi", "Stitch", "Pepa Pig",
             "Bowser", "potato head", ]

list1 = (list(string.ascii_letters))
guessed_letters = []
string = (random.choice(word_bank))
"-".join(string)
word = "-" * len(string)
print(word)
guess = input("Take a guess: ")

win = False
turn = 8
guessed = 8
current_index = word.index(word)

while turn > 0 and not word:
    guessed -= 1
    for character in range(len(word)):
        if guess.lower() == word:
            guess.append(guessed_letters)
            string.pop(current_index)
            string.insert(current_index, guess)
            print(word)

        elif guess.upper() == word:
            string.pop(current_index)
            string.insert(current_index, guess)
            print(word)
            input("Take another guess")
        elif guess != word:
