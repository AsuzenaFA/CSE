import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
win = False
bank = 50
roll = int
rolling = dice1 and dice2
int(input("Type 'roll' to throw the dice:  "))
while rolling:
    if dice1 + dice2 == 7:
        win = True
        bank = bank + 10
    elif dice1 + dice2 < 7:
        win = False
        bank = bank - 10
    elif dice1 + dice2 > 7:
        win = False
        bank = bank - 10
