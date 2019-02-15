class Sword(object):
    def __init__(self, damage=10, speed=5, swing=0, stamina=100):
        self.damage = damage
        self.speed = speed
        self.grip = True
        self.stamina = stamina
        self.swing = swing

    def shoot(self):
        if self.grip:
            self.swing += 1
            if self.stamina == 0:
                print("You have no stamina")
            elif self.stamina < self.swing:
                print("You ran out f stamina and swung %s times" % self.swing)
        else:
            print("Yuo have no grip")

    def wait(self):
        self.stamina = 100
        print("You regained all your stamina")

my_sword(10, )