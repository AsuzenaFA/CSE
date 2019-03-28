import Player

class Item(object):
    def __init__(self, name, condition):
        self.name = name
        self.durability = condition
        self.equipped = False


class Sword(Item):
    def __init__(self, name, condition, damage):
        super(Sword, self).__init__(name, condition)
        self.durability = 100
        self.equipped = False
        self.damage = damage
        self.stamina = Player

    def grip(self):
        self.equipped = True
        print("You have the sword in your hands")

    def swing(self):
        self.stamina -= 10
        print("You swing and lose stamina")

    def stun(self):
        self.stamina -= 5
        print("You stunned the enemy and lost stamina")

    def block(self):
        self.stamina -= 3
        print("You block and lose stamina")

    def put_away(self):
        self.equipped = False
        print("You put the sword away")


class BroadSword(Sword):
    def __init__(self):
        super(BroadSword, self).__init__("Broad Sword", 100, 30)


class Dagger(Sword):
    def __init__(self):
        super(Dagger, self).__init__("Thief's Dagger", 50, 10)


class Katana(Sword):
    def __init__(self):
        super(Katana, self).__init__("Katana", 80, 18)


class VikingSword(Sword):
    def __init__(self):
        super(VikingSword, self).__init__("Viking Sword", 100, 20)


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__("Long Sword", 90, 25)


class Potion(Item):
    def __init__(self, name, amount, condition, potion_effect):
        super(Potion, self).__init__(name, condition)
        self.durability = 1
        self.size = amount
        self.effect = potion_effect
        self.drink = False

    def drink(self):
        self.drink = True


class BigHealth(Potion):
    def __init__(self):
        super(BigHealth, self).__init__("Big Health Potion", 10, 1, "Health")
        self.healing_amt = 10


class SmallHealth(Potion):
    def __init__(self):
        super(SmallHealth, self).__init__("Small Health Potion", 5, 1, "Health")
        self.healing_amt = 5


class BigMana(Potion):
    def __init__(self):
        super(BigMana, self). __init__("Big Mana Potion", 10, 1, "Mana")
        self.mana_amt = 10


class SmallMana(Potion):
    def __init__(self):
        super(SmallMana, self).__init__("Small Mana Potion", 5, 1, "Mana")
        self.mana_amt = 5


class BigStamina(Potion):
    def __init__(self):
        super(BigStamina, self).__init__("Big Stamina Potion", 10, 1, "Stamina")
        self.Stamina_amt = 10


class SmallStamina(Potion):
    def __init__(self):
        super(SmallStamina, self).__init__("Small Stamina Potion", 5, 1, "Stamina")
        self.Stamina_amt = 5


class Restoration(Potion):
    def __init__(self):
        super(Restoration, self).__init__("Restoration Potion", 20, 1, "Restoration")
        self.mana_amt = 20
        self.stamina_amt = 20
        self.healing_amt = 20


class Armor(Item):
    def __init__(self, name, kind, condition, weight):
        super(Armor, self).__init__(name, condition)
        self.kind = kind
        self.equipped = False
        self.weight = weight

    def protection(self):
        self.equipped = True


class LeatherArmor(Armor):
    def __int__(self):
        super(LeatherArmor, self).__init__("Leather Armor", "Leather", 500, 10)


class IronArmor(Armor):
    def __int__(self):
        super(IronArmor, self).__init__("Iron Armor", "Iron", 1000, 50)


class ThiefArmor(Armor):
    def __int__(self):
        super(ThiefArmor, self).__init__("Thief", "Thief", 300, 20)


class DragonArmor(Armor):
    def __init__(self):
        super(DragonArmor, self).__init__("Dragon Scale Armor", "Scales", 5000, 40)


class AncientArmor(Armor):
    def __init__(self):
        super(AncientArmor, self).__init__("Ancient Armor", "old", 200, 10)


 class BarrierPendant(Armor):
     def __init__(self):
        super(BarrierPendant, self).__init__("Barrier Pendent", "Magic", 7000000, None)


class Axes(Item):
    def __init__(self, name, condition, damage):
        super(Axes, self).__init__(name, condition)
        self.damage = damage
        self.stamina = Player
        self.equipped = False


class Tomahawk(Axes):
    def __init__(self):
        super(Tomahawk, self).__init__("Tomahawk", 500, 30)


class Hatchet(Axes):
    def __init__(self):
        super(Hatchet, self).__init__("Hatchet", 1000, 10)


class BattleAxe(Axes):
    def __init__(self):
        super(BattleAxe, self).__init__("Battle Axe", 2000, 50)

    def grip(self):
        self.equipped = True

    def swing(self):
        self.stamina -= 5
        print("You swing and lose 5 stamina")

    def stun(self):
        self.stamina -= 2
        print("You stun the enemy and lose 2 stamina")


class WeirdStuff(Item):
    def __init__(self, name, description):
        super(WeirdStuff, self).__init__(name, condition=None)
        self.description = description
        self.examine = True


def examine(self):
    if self.examine:
        print('description')


class MammothTusk(WeirdStuff):
    def __init__(self):
        super(MammothTusk, self).__init__("Ancient Mammoths Tusk", "With all the three pices of the tusk together you "
                                                                   "can now read the craving on it, the tusk says,"
                                                                   ""
                                                                   "'Property of MK'"
                                                                   "MK Stands for the Magma King"
                                                                   "You should return it")


class MTP1(WeirdStuff):
    def __init__(self):
        super(MTP1, self).__init__("Tusk Part 1", "You Bought this 'Elephant Tusk' at a Merchants shop"
                                                  ", it has the word 'Pro' carved in at the side")


class MTP2(WeirdStuff):
    def __init__(self):
        super(MTP2, self).__init__("Tusk Part 2", "You found this tusk part in a tar pit, it had tar in the carving"
                                                  " but you can read it and it says"
                                                  " 'perty'")


class MTP3(WeirdStuff):
    def __init__(self):
        super(MTP3, self).__init__("Tusk part 3", "You found this in the swamp area on top of a pile of bones")


class PinkEgg(WeirdStuff):
    def __init__(self):
        super(PinkEgg, self).__init__("Pink Wyvern Egg", "This is the egg you collected in the Wyverns Cave")


class BlackBearSkin(WeirdStuff):
    def __init__(self):
        super(BlackBearSkin, self).__init__("Black Bear Skin", "This is a Bear skin that you found at the entrance"
                                                               " of the wasteland"
                                                               " The inside of it says 'Rat King's'")

