
import string
import random
word_bank = ["pink dolphin", "Spongebob", "Aurthor", "Princess Peach", "Mario", "Bambi", "Stitch", "Pepa Pig",
             "Bowser", "potato head", ]

guessed_letters = []
list1 = (list(string.ascii_letters))
word = (random.choice(word_bank))
word_list = list(word)
" ".join(word)
word_list = "-", len(word_list)
scores_list = list(word_list)

print(word)
