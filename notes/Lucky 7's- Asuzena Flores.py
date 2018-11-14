import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
rounds = 0
win = False
bank = 15
while bank > 0:
    rounds += 1
    if dice1 + dice2 == 7:
        win = True
        bank = bank + 4
    elif dice1 + dice2 < 7:
        win = False
        bank = bank - 1
    elif dice1 + dice2 > 7:
        win = False
        bank = bank - 1
        print(dice1 + dice2)
print("Your current amount is %s." % bank)

