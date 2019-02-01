import random
word_bank = ["pink dolphin", "spongebob", "arthur", "princess peach", "mario", "bambi", "stitch", "pepa pig",
             "bowser", "potato head", ]

guessed_letters = []
string = random.choice(word_bank)
list_of_letters = list(string.lower())
word = list("-" * len(string))
print("".join(word))

win = False
turn = 8


while turn > 0 and not win:
    current_guess = input("Take a guess: ")
    turn -= 1
    guessed_letters.append(current_guess)
    if current_guess.lower() in list_of_letters:
        print("CORRECT!")
        for pos in range(len(word)):
            if list_of_letters[pos].lower() == current_guess.lower():
                word.pop(pos)
                word.insert(pos, list_of_letters[pos])
                print("".join(word))
    elif current_guess not in word:
        print("WRONG")
    elif current_guess is word:
        win = True
        print("You guessed it, the word was %s" % word)
    elif turn < 0:
        win = False
        if turn < 0:
            print("You lose")
