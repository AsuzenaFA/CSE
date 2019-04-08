class Room(object):
    def __init__(self, name, north, south, east, west, description, character=None, enemy=None,items=None):
        if items is None:
            items = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.character = character
        self.items = items
        self.enemy = enemy


class Item(object):
    def __init__(self, name, condition):
        self.name = name
        self.durability = condition
        self.equipped = False


def take():
    _found_item = None
    if player.current_location.items is not None:
        if player.current_location.items.name.lower() == found_item.lower():
            _items_found = player.current_location.items
    if isinstance(found_item, Item):
        print("You picked up " + _found_item.name)
        player.inventory.append(found_item)
        player.current_location.item = None


def drop():
    _found_item = None
    for item in player.inventory:
        if item.name.lower() == _found_item.lower():
            _found_item = item
            print("You dropped the item %s" % item.name)
    if found_item is not None:
        if player.current_location.item is None:
            player.current_location.item = found_item
            player.inventory.remove(found_item)
        else:
            print("That item is already in there.")
    else:
        print("You don't have this item.")


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
        super(MTP1, self).__init__("Tusk Part 1", "You got this 'Elephant Tusk' at a Merchants shop"
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
    def __init__(self, attack):
        self.stamina = 100
        self.attack = attack
        self.health = 100

    def turn(self):
        self.stamina -= 10
        if self.turn == 0:
            self.attack = 0


class Ogre(Enemy):
    def __init__(self):
        super(Ogre, self).__init__(5)


class GiantToads(Enemy):
    def __init__(self):
        super(GiantToads, self).__init__(3)


class Moles(Enemy):
    def __init__(self):
        super(Moles, self).__init__(4)


class Rats(Enemy):
    def __init__(self):
        super(Rats, self).__init__(6)


class Roach(Enemy):
    def __init__(self):
        super(Roach, self).__init__(4)


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
        print(self.name)
        print("Hey what are you doing in here")


class Thief2(Character):
    def __init__(self):
        super(Thief2, self).__init__("Dos", 90, Dagger, ThiefArmor)
        print(self.name)
        print("Yah your and outsider. This place isn't for you"
              " are you lost")


class Thief3(Character):
    def __init__(self):
        super(Thief3, self).__init__("Tres", 90, Dagger, ThiefArmor)
        print(self.name)
        print("...")


class Shops(object):
    def __init__(self, name):
        self.name = name


class BSS(Shops):
    def __init__(self):
        super(BSS, self).__init__("Iron's Shop")
        self.storage = {}

    def ask(self):
        print("Hey welcome to %s , what would you like to buy." % self.name)
        _command_ = input(">_")
        if command in ['buy']:
            print("This is what we have: ")
            for item in self.storage:
                print(self.storage[item]["Name"] + "-" + str(self.storage[item]["Cost"] + "$"))
            request = input("I want to buy a > ")
            for i, thing in enumerate(self.storage.keys()):
                if self.storage[thing]["Name"] == request:
                    customer_i = input("Do you want to but the %s " % self.storage[thing]["Name"])
                    if customer_i in ['yes']:
                        if player.money >= self.storage[thing]["Cost"]:
                            print("You bought and item for %d coins" % self.storage[thing]["Cost"])
                            print("You have %d coins left" % player.money)
                            player.inventory.append(self.storage[thing]["ID"])
                        elif player.money < self.storage[thing]["Cost"]:
                            if player.money <= 0:
                                print("You have no money")
                            else:
                                print("You only have %d on you" % player.money)
                                self.ask()


class BlackSmithShop(Shops):
    def __init__(self):
        super(BlackSmithShop, self).__init__("Coppers Blacksmith")
        self.storage = {
            "stock1": {
                "Name": Battle_Axe.name,
                "Cost": 10,
                "ID": BattleAxe
            },
            "stock2": {
                "Name": Viking_Sword.name,
                "Cost": 10
            },
            "stock3": {
                "Name": Long_Sword.name,
                "Cost": 5
            },
            "stock4": {
                "Name": Katana.name,
                "Cost": 9
            }


        }


class MerchantShop(Shops):
    def __init__(self):
        super(MerchantShop, self).__init__("Clerk's Stuff and More")
        self.storage = {
            "stock1"
        }


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

# Werid Items
Pink_Egg = PinkEgg()
Black_Bear_Skin = BlackBearSkin()
MTP1 = MTP1()
MTP2 = MTP2()
MTP3 = MTP3()
Mammoth_Tusk = MammothTusk()

# Characters
Character = Mute()
Character2 = Doctor()
Character3 = Merchant()
Character4 = BlackSmith()
# Rooms

Spawn = Room("Your Cabin", None, None, 'Lawn', 'Backyard',
             "You are in your house with your backpack on "
             "it has two exits one to the east and one to the west", [Long_Sword])

Backyard = Room("Your backyard", 'North_Forest', 'Water_Fountain', 'West_Forest', 'Spawn',
                "You look around and there is a hatchet in a log and there is"
                " forest to the west, north, and a water fountain to the south.", [Hatchet])

NF = Room("Northern Forest", 'Grass Trail', 'Gates', 'Tar_Rivers', None,
          "Your in a quiet forest and you hear grass hoppers to the north")

WF = Room("Western Forest", 'Grass Trail', 'Pond', 'Spawn', None,
          "You in what once was a forest but is now a bunch of stumps and you hear"
          "frogs to the south")

EF = Room("Eastern Forest", 'Trench', 'Swamp', 'BB', 'Water_Fountain',
          "Your in a forest and hear a bubbling noise to the east")

SF = Room("Southern Forest", 'Ware_Fountain', 'Swamp', 'FT', 'Dense_Forest',
          "You are in a forest, there's nothing special about it")

Lawn = Room("Your Lawn", 'North_Forest', 'Water_Fountain', 'Gates', 'Spawn',
            "You look around and see the water fountain to the south, forest to the north,and a big wooden"
            "gate to the east.")

Water_Fountain = Room("Broken Water Fountain", 'Spawn', 'Swamp', 'East_Forest', 'West_Forest',
                      "The fountain seems to be broken. You look around to see forest to the south, west, and east")

Tar_River = Room("Tar River", 'BB', 'FT', None, 'EF',
                 "You are at a long river of tar, you see a bridge to the north"
                 " and a a tree over the river to the south")

BB = Room("Broken Bridge", 'Trench', 'FT', None, 'EF',
          "You walk onto the bridge but see the it is broken so you get off")

FT = Room("Fallen Tree", 'BB', None, 'Tar_Pit', 'Swamp',
          "You are at the Fallen Tree, it looks like someone had put it there,"
          " it looks stable and you can go over it, there is also a huge wall "
          "to the south the you cant climb", [Battle_Axe])

Tar_Pit = Room("Tar Pit", 'Wasteland', 'Revine', None, 'FT',
               "Your at a tar pit a bit away from the tar river, you see something sticking out of the pit",
               [MTP2])

Revine = Room("Wyvern's Cave", 'Tar_Pit', None, None, None,
              "You wonder into a revine, its very hot, you see a sliver "
              "of light in the wall and you walk towards it..."
              "When you reach the other side you are surrounded by wyverns", [Pink_Egg])

WastelandE = Room("The Wasteland Entrance", 'FOW', 'Tar_Pit', None, 'Rope_Bridge',
                  "You are at the front of what looks like a run down city. The entence is a broken fence "
                  "and you cna go in, but there is a weird fuzzy thing stuck in the fence", [Black_Bear_Skin])

FOW = Room("Evergreen Road", 'MOW', 'WastelandE', None, None,
           "You walk into the place and you are walking down a road..."
           "You are surrounded but 3 thieves", [])

Gates = Room("Front Gates", 'HT', 'Merchant', 'BV', 'Lawn',
             "you are at the front fo the village, "
             "you see a doctor with nurses and a big oak tree behind them to the north, "
             "a merchant to the south, and a castle far towards the east")

HT = Room("Doctor's Healing Tree", None, 'Gates', None, None,
          "You walk up to the area but are blocked bya nurse, the doctor "
          "comes up to you", Doctor)

Merchant = Room("Clerk's Items and More", 'Gates', None, None, None,
                "You enter the creepy Item Shop, you see many useless items"
                " sword with weird carvings", )

BV = Room("Back of Village", 'Blacksmith', 'Tavern', 'Kings_Castle', None,
          "You walk more in to the and see a tavern to the north, a blacksmith to the south,"
          " and the castle in the east")

Tavern = Room("Mute's Tavern", None, BV, None, None,
              "You walk into the tavern and sit at the bar, "
              "there is a bartender serving other people", Mute)

Blacksmith = Room("Jacks Weapons and Armory", None, 'BV', None, None,
                  "You walk up to the workshop and see a man working on "
                  "a sword", BlackSmith, [])

Kings_Castle = Room("Castle", None, None, None, 'BV', "The Room is empty but you see a hole in the floor")


# Players
player = Player(Spawn)
player.weapon = Dagger

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
PlayerActions = ['give', 'talk', 'take', 'drop', 'buy']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print()
    if player.current_location.items is not None:
        print("There is a %s in here" % player.current_location.items)
    else:
        print("There is nothing in this room")

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif "take" in command:
        found_item = command[5:]
        take()
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
