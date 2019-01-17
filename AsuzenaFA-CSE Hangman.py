import string
import random
word_bank = ["pink dolphin", "spongebob", "aurthor", "princess peach", "mario", "bambi", "stitch", "pepa pig",
             "bowser", "potato head", ]
character = (list(string.ascii_letters))
guessed_letters = []
string1 = (random.choice(word_bank))
list1 = (list(string1))
print(" ".join(string1))
print(input("Type in a letter: "))

win = False
turn = 8
guessed = turn - 1

for character in range(len(word_bank)):
    if character == list1:
        current_index = list.index(character)
        list1.pop(current_index)
        list.insert(current_index, "-")
        print(" ".join(string1))

while turn > 0:
    turn = guessed
    if turn == 0:
        win = False
        print("You lose")
