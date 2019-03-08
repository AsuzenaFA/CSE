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
        self.stamina = Character

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


class Character(object):
    def __init__(self, talk):
        self.talk = talk
        self.charge = 10

    class Player(object):
        def __init__(self, starting_location):
            self.current_health = 100
            self.current_location = starting_location
            self.inventory = []
            self.damage = 5
            self.stamina = 100
            self.money = 100
            self.manna = 100
            self.armor = 0

        def move(self, new_location):
            """This method moves a character to a new location

            :param new_location:  The variable containing a room
            """
            self.current_location = new_location
