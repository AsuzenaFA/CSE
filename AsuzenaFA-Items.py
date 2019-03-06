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
        super(BroadSword, self).__init__("Broad Sword", 100, 15)


class Dagger(Sword):
    def __init__(self):
        super(Dagger, self).__init__("Thief's Dagger", 50, 20)


class Katana(Sword):
    def __init__(self):
        super(Katana, self).__init__("Katana", 80, 18)





class Character(object):
    def __init__(self, talk):
        self.talk = talk
        self.charge = 10

    class Player(object):
        def __init__(self, starting_location):
            self.health = 100
            self.current_location = starting_location
            self.inventory = []
            self.damage = 5
            self.stamina = 100
            self.money = 100
            self.manna = 100

        def move(self, new_location):
            """This method moves a character to a new location

            :param new_location:  The variable containing a room
            """
            self.current_location = new_location
