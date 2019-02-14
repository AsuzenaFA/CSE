class Sword(object):
    def __init__(self, damage=10, speed=5, durability=50, stamina=100, distance=5):
        self.damage = damage
        self.range = distance
        self.speed = speed
        self.durability = durability
        self.grip = True
        self.stamina = stamina

    def shoot(self):
        if self.grip:
            if self.range <= self.stamina:
                print()