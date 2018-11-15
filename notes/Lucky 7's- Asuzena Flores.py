import random
roll_again = "yes"
bank = 15
rounds = 0
while bank > 0:
    print("Rolling Dice...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("You got")
    print(dice1)
    print(dice2)
    rounds += 1
    bank -= 1
    myrole = (dice1 + dice2)
    if myrole == 7:
        bank += 5
        print("You got 7 you got 4 dollars." )
    elif myrole != 0:
        print("You didn't get a 7, roll again? ")
    elif bank != 0:
        print("You don't have enough money")
print("You lose, you played for %d rounds" % rounds)
