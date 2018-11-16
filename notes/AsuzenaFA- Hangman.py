import 
word = random
guess = ''
turns = 10
print(" The word has 5 letters take a guess: ")
while turns > 0:
    if guess is not word:
        turns -= 1
        print("No that, take another guess: ")
    if guess is word:
        win = True
        print("You guessed it you win.")
