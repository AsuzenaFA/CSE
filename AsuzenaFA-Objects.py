class Sword(object):
    def __init__(self, damage=10, speed=5, swing=0, stamina=100):
        self.damage = damage
        self.speed = speed
        self.grip = True
        self.stamina = stamina
        self.swing = swing

    def shoot(self):
        if self.grip:
            self._check_swings()
            if self.stamina <= 0:
                print("You have no stamina")
            elif self.stamina < self.swing:
                print("You ran out of stamina and swung %s times" % self.swing)
                self.stamina = 0
            else:
                print("You swing the sword")
                self.stamina -= 10
        else:
            print("Yuo have no grip")

    def wait(self):
        if self.stamina == 0:
            self.stamina = 100
            print("You regained all your stamina")

    def _check_swings(self):
        if self.swing >= 10:
            self.grip = False
            print("The grip broke.")
        else:
            self.swing += 1


my_sword = Sword(10, 5, 5)
my_sword.shoot()
