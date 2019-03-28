class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.talk = False
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.give = False
        self.charge = False
        self.name = name

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %s health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon))
        target.take_damage(self.weapon.damage)


class Mute(Character):
    def __init__(self):
        super(Mute, self).__init__("Mute", 9999999999999999999, PlasmaPumpShotgun, BarrierPendant)
        if self.talk:
            print("...")


class Merchant(Character):
    def __init__(self):
        super(Merchant, self).__init__("Token Coin", 99999999999999999, LongSword, BarrierPendant)
        if self.talk:
            print("Hey, what would you like to buy.")


class BlackSmith(Character):
    def __init__(self):
        super(BlackSmith, self).__init__("Ronald Iron", 9999999999999999, BattleAxe, BarrierPendant)


class Doctor(Character):
    def __init__(self):
        super(Doctor, self).__init__("Dr. Roger", 50, None, None)
        if self.talk:
            print("Hey you can't go near that tree with out paying, give me 100 coin and i'll let you in")


class Thief1(Character):
    def __init__(self):
        super(Thief1, self).__init__("Uno", 90, Dagger, ThiefArmor)


class Thief2(Character):
    def __init__(self):
        super(Thief2, self).__init__("Dos", 90, Dagger, ThiefArmor)


class Thief3(Character):
    def __init__(self):
        super(Thief3, self).__init__("Tres", 90, Dagger, ThiefArmor)
