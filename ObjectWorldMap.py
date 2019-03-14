class Room(object):
    def __init__(self, name, north, south, east, west, description, character=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.character = character
        self.items = []


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
        self.target = Enemy

    def grip(self):
        self.equipped = True
        print("You have the sword in your hands")

    def swing(self):
        self.stamina -= 10
        print("You swing and lose stamina")
        self.durability -= 1

    def stun(self):
        self.stamina -= 5
        print("You stunned the enemy and lost stamina")

    def block(self):
        self.stamina -= 3
        print("You block and lose stamina")

    def put_away(self):
        self.equipped = False
        print("You put the sword away")


class Enemy(object):
    def __init__(self):
        self.turn = 10
        self.attack = 2
        self.health = 100

    def turn(self):
        self.turn -= 1
        if self.turn == 0:
            self.attack = 0


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


class Axes(Item):
    def __init__(self, name, condition, damage):
        super(Axes, self).__init__(name, condition)
        self.damage = damage
        self.stamina = Character
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
    def __init__(self):
        super(LeatherArmor, self).__init__("Leather Armor", "Leather", 500, 10)


class IronArmor(Armor):
    def __init__(self):
        super(IronArmor, self).__init__("Iron Armor", "Iron", 1000, 50)


class ThiefArmor(Armor):
    def __init__(self):
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


class Guns(Item):
    def __init__(self, name, condition, capacity, damage):
        super(Guns, self).__init__(name, condition)
        self.equipped = False
        self.trigger = False
        self.durability = condition
        self.damage = damage
        self.capacity = capacity

    def shoot(self):
        self.capacity -= 1
        if self.capacity <= 0:
            print("You have no bullets, you need to reload")

    def reload(self):
        self.capacity = 2
        print("You reloaded")


class PlasmaPumpShotgun(Guns):
    def __init__(self):
        super(PlasmaPumpShotgun, self).__init__("Plasma Pump Shotgun", 1000, 2, 100)


class Character(object):
    def __init__(self, name, talk, health, weapon, armor):
        self.talk = talk
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
        super(Mute, self).__init__("Mute", False, 9999999999999999999, PlasmaPumpShotgun, BarrierPendant)
        if self.talk:
            print("...")

class Merchant(Character):
    def __init__(self):
        super(Merchant, self).__init__("Token Coin", False, 99999999999999999, LongSword, BarrierPendant)
        if self.talk:
            print("Hey, what would you like to buy.")

class BlackSmith(Character):
    def __init__(self):
        super(BlackSmith, self).__init__("Ronald Iron", False, 9999999999999999, BattleAxe, BarrierPendant)

class Doctor(Character):
    def __init__(self):
        super(Doctor, self).__init__("Dr. Roger", True, 50, None, None)
        if self.talk:
            print("Hey you can't go near that tree with out paying, give me 100 coin and i'll let you in")



class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 5
        self.stamina = 100
        self.money = 100
        self.manna = 100
        self.weapon = None

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location:  The variable containing a room
        """
        self.current_location = new_location


# Instantiate Items
Dragon_Armor = DragonArmor()
Ancient_Armor = AncientArmor()
Thief_Armor = ThiefArmor()
Iron_Armor = IronArmor()
Leather_Armor = LeatherArmor()

Big_Health = BigHealth()
Small_Health = SmallHealth()
Big_Mana = BigMana()
Small_Mana = SmallMana()
Big_Stamina = BigStamina()
Small_Stamina = SmallStamina()

Tomahawk = Tomahawk()
Hatchet = Hatchet()
Battle_Axe = BattleAxe()

Long_Sword = LongSword()
Broad_Sword = BroadSword()
Dagger = Dagger()
Viking_Sword = VikingSword()
Katana = Katana()

# Characters
Character = Mute()
Character2 = Doctor()
Character3 = Merchant()
CHaracter4 = 
# Rooms
Spawn = Room("Your Cabin", None, None, 'Lawn', 'Backyard',
             "You are in your house with your backpack on "
             "it has two exits one to the east and one to the west",)

Backyard = Room("Your backyard", 'North_Forest', 'Water_Fountain', 'West_Forest', 'Spawn',
                "You look around and there is a hatchet in a log and there is"
                " forest to the west, north, and a water fountain to the south.", )

NF = Room("Northern Forest", 'Grass Trail', 'Gates', 'Tar_Rivers', 'Desert',
          "Your in a quiet forest and you hear grass hoppers to the north")

WF = Room("Western Forest", 'Grass Trail', 'Pond', 'Spawn', 'Desert',
          "You in what once was a forest but is now a bunch of stumps and you hear"
          "frogs to the south")

Desert = Room("Desert", None, None, None, 'D1',
              "You walked into a desert and don't know where you are, suddenly stone"
              " walls rise up from the ground, you are now in a maze")

EF = Room("Eastern Forest", 'Trench', 'Swamp', 'BB', 'Water_Fountain',
          "Your in a forest and hear a bubbling noise to the east")

SF = Room("Southern Forest", 'Ware_Fountain', 'Swamp', 'FT', 'Dense_Forest',
          "You are in a forest")

Lawn = Room("Your Lawn", 'North_Forest', 'Water_Fountain', 'Gates', 'Spawn',
            "You look around and see the water fountain to the south, forest to the north,and a big wooden"
            "gate to the east.")

Water_Fountain = Room("Broken Water Fountain", 'Spawn', 'Swamp', 'East_Forest', 'West_Forest',
                      "The fountain seems to be broken. You look around to see forest to the south, west, and east")

Tar_River = Room("Tar River", 'BB', 'Fallen_Tree', None, 'EF',
                 "You are at a long river of tar, you see a bridge to the north"
                 " and a a tree over the river to the south")

BB = Room("Broken Bridge", 'Trench', 'FT', None, 'EF',
          "You walk onto the bridge but see the it is broken so you get off")

FT = Room("Fallen Tree", 'BB', None, 'Ravine', 'Swamp',
          "You are at the Fallen Tree, it looks like someone had put it there,"
          " it looks stable and you can go over it, there is also a huge wall "
          "to the south the you cant climb")

Gates = Room("Front Gates", 'HT', 'Merchant', 'BV', 'Lawn',
             "you are at the front fo the village, "
             "you see a doctor with nurses and a big oak tree behind them to the north, "
             "a merchant to the south, and a castle far towards the east")

HT = Room("Doctor's Healing Tree", None, 'Gates', None, None,
          "You walk up to the area but are blocked by a nurse, the doctor "
          "comes up to you and says you need to pay to get by the fence")

Merchant = Room("Clerk's Items and More", 'Gates', None, None, None,
                "You enter the creepy Item Shop, you see many useless items but then see an elephant tusk"
                " sword with weird carvings")

BV = Room("Back of Village", 'Blacksmith', 'Tavern', 'Kings_Castle', None,
          "You walk more in to the and see a tavern to the north, a blacksmith to the south,"
          " and the castle in the east")

Tavern = Room("Mute's Tavern", None, BV, None, None,
              "You walk into the tavern and sit at the bar, "
              "there is a bartender serving other people")

Blacksmith = Room("Jacks Weapons and Armory", 'BV', None, None, None,
                  "You walk up to the workshop and see a man working on "
                  "a sword")

Kings_Castle = Room("Castle", None, None, None, 'BV', "The Room is empty but you see a hole in the floor")


# Players
player = Player(Spawn)
player.weapon = Dagger

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
actions = ['give', 'take', 'talk']
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]
            player.move(room_object)
        except KeyError:
            print("This key dose not exist")
        except AttributeError:
            print("I can't go that way.")
    else:
        print("Command not recognized")

