import random
word_bank = ["pink dolphin", "Spongebob", "Arthur", "Princess Peach", "Mario", "Bambi", "Stitch", "Pepa Pig",
             "Bowser", "potato head", ]

guessed_letters = []
string = random.choice(word_bank)
list_of_letters = list(string.lower())
word = list("-" * len(string))
print("".join(word))
guess = input("Take a guess: ")

win = False
turn = 8


while turn > 0 and not win:
    current_guess = input("Take a guess: ")
    turn -= 1
    guessed_letters.append(guess)
    if current_guess.lower() in list_of_letters:
        print("CORRECT!")
        for pos in range(len(word)):
            if list_of_letters[pos].lower() == current_guess.lower():
                word.pop(pos)
                word.insert(pos, list_of_letters[pos])
                print("".join(word))
    elif current_guess.upper() in list_of_letters:
        print("CORRECT!")
        for pos in range(len(word)):
            if list_of_letters[pos].upper() == current_guess.upper():
                word.pop(pos)
                word.insert(pos, list_of_letters)
                print("".join(word))
    if current_guess in guessed_letters:
        print("You already guessed that")
    elif current_guess not in word:
        print("WRONG")

    if turn < 0:
        win = False
    elif turn < 0:
        print("You lose")
    elif current_guess is word:
            win = True
            print("You guessed it, the word was %s" % word)
