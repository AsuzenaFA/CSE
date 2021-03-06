class Room(object):
    def __init__(self, name, north, south, east, west, description, character, items=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.character = character
        self.items = items


class Item(object):
    def __init__(self, name, condition):
        self.name = name
        self.durability = condition
        self.equipped = False


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


class Seeds(WeirdStuff):
    def __init__(self):
        super(Seeds, self).__init__("Seeds", "These are the seeds you found in the farm")


class EC(WeirdStuff):
    def __init__(self):
        super(EC, self).__init__("Energy Coals", "These are the weird coals tht you found in the mines.")


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


class BroadSword(Sword):
    def __init__(self):
        super(BroadSword, self).__init__("Broad Sword", 100, 30)


class Dagger(Sword):
    def __init__(self):
        super(Dagger, self).__init__("Tres's Dagger", 50, 10)


class Katana(Sword):
    def __init__(self):
        super(Katana, self).__init__("Levy's Katana", 80, 18)


class VikingSword(Sword):
    def __init__(self):
        super(VikingSword, self).__init__("Token's Sword", 100, 20)


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


class DragonArmor(Armor):
    def __init__(self):
        super(DragonArmor, self).__init__("Dragon Scale Armor", "Scales", 5000, 40)


class AncientArmor(Armor):
    def __init__(self):
        super(AncientArmor, self).__init__("Ancient Armor", "old", 100000, 20)


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


class Scrolls(Item):
    def __init__(self, name, quests):
        super(Scrolls, self).__init__(name, condition=None)
        self.name = name
        self.quests = quests

    def read(self):
        print(self.name)
        print("---The scroll says---")
        print(self.quests)


class Scroll1(Scrolls):
    def __init__(self):
        super(Scroll1, self).__init__("The Bear Skin", "Go to the Wastelands and find Rat Kings Bear Coat.")


class Scroll2(Scrolls):
    def __init__(self):
        super(Scroll2, self).__init__("The tusk", "Find all the mammoth tusk parts and return it to the owner.")


class Character(object):
    def __init__(self, name, health, weapon, armor, inventory=[]):
        self.talk = False
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.give = False
        self.charge = False
        self.name = name
        self.inventory = inventory

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
            print("Hey your new here, do you mind doin me a favor and take this letter to the "
                  "group of people that live in a tree house, they're in the north-western part of the land.")


class Merchant(Character):
    def __init__(self):
        super(Merchant, self).__init__("Token Coin", 99999999999999999, LongSword, BarrierPendant)
        if self.talk:
            print("Hey new comer welcome to my shop, oh you have that mark on your neck, well i guess you can"
                  " take what ever you like... the thing here aren't that useful.")


class BlackSmith(Character):
    def __init__(self):
        super(BlackSmith, self).__init__("Ronald Iron", 9999999999999999, BattleAxe, BarrierPendant)
        if self.talk:
            print("...")


class Doctor(Character):
    def __init__(self):
        super(Doctor, self).__init__("Dr. Roger", 50, None, None)
        if self.talk:
            print("Hey you can't go near that tree with out paying, give me 100 coin and i'll let you in")


class Thief1(Character):
    def __init__(self):
        super(Thief1, self).__init__("Uno", 90, Dagger, None)
        print(self.name)
        print("Hey what are you doing in here")


class Thief2(Character):
    def __init__(self):
        super(Thief2, self).__init__("Dos", 90, Dagger, None)


class Thief3(Character):
    def __init__(self):
        super(Thief3, self).__init__("Tres", 90, Dagger, None)
        print(self.name)


class Helper(Character):
    def __init__(self):
        super(Helper, self).__init__("Elijah", 1000000000000, PlasmaPumpShotgun, BarrierPendant)


class RatKing(Character):
    def __init__(self):
        super(RatKing, self).__init__("Rat King", 100000000000, PlasmaPumpShotgun, BarrierPendant)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 5
        self.money = 100

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location:  The variable containing a room
        """
        self.current_location = new_location


# Instantiate Items
Dragon_Armor = DragonArmor()
Ancient_Armor = AncientArmor()
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
Seeds = Seeds()
EC = EC()

# Scrolls
Scroll_1 = Scroll1()
Scroll_2 = Scroll2()

# Characters
Character = Mute()
Character2 = Doctor()
Character3 = Merchant()
Character4 = BlackSmith()
Character5 = Helper()
# Rooms

Spawn = Room("Your Cabin", None, None, 'Lawn', 'Backyard',
             "You are in your house with your backpack on "
             "it has two exits one to the east and one to the west"
             ""
             " == Elijah is in the room ==", Helper, Long_Sword)

Backyard = Room("Your backyard", 'NF', 'Water_Fountain', 'Spawn', 'WF',
                "You look around and there is a hatchet in a log and there is"
                " forest to the west, north, and a water fountain to the south.", None, Hatchet)

NF = Room("northern Forest", 'Grass Trail', 'Gates', 'Tar_Rivers', 'WF',
          "Your in a quiet forest and you hear grass hoppers to the north", None)

WF = Room("Western Forest", 'NF', 'SF', 'Backyard', 'Creek',
          "You in what once was a forest but is now a bunch of stumps and you hear"
          "frogs to the south", None)

Creek = Room("Creek", 'FBL', 'Dense_Forest', 'WF', None,
             "You are at a creek on  east side of the"
             "land.", None, Katana)

FBL = Room("Frost bite lands", 'Rocko', 'Creek', None, None, "Its cold", None)

Rocko = Room("Village of Rocko", 'FBl', None, None, None, "A village full of orcs.", None)

EF = Room("Eastern Forest", 'NF', 'SF', 'Tar_River', None,
          "Your in a forest and hear a bubbling noise to the east", None)

SF = Room("Southern Forest", 'Water_Fountain', 'AB_Farm', 'EF', 'East_Dense_Forest',
          "You are in a forest, there's nothing special about it", None)

Lawn = Room("Your Lawn", 'North_Forest', 'Water_Fountain', 'Gates', 'Spawn',
            "You look around and see the water fountain to the south, forest to the north,and a big wooden"
            "gate to the east.", None)

Water_Fountain = Room("Broken Water Fountain", 'Backyard', 'SF', 'East_Forest', 'West_Forest',
                      "The fountain seems to be broken. You look around to see forest to the south, west, and east",
                      None)

Tar_River = Room("Tar River", 'BB', 'FT', None, 'EF',
                 "You are at a long river of tar, you see a bridge to the north"
                 " and a a tree over the river to the south", None)

BB = Room("Broken Bridge", 'RB', 'FT', None, 'EF',
          "You walk onto the bridge but see the it is broken so you get off", None)

FT = Room("Fallen Tree", 'BB', 'Mines', 'Tar_Pit', 'Farm',
          "You are at the Fallen Tree, it looks like someone had put it there,"
          " it looks stable and you can go over it, there is also a stump"
          " near by with a battle axe in it", None, Battle_Axe)

Mines = Room("Coal Mines", 'FT', None, None, 'Swamp', "Your in the Coal Mines", None, EC)

Farm = Room("Abandoned Farm", 'SF', 'Swamp', 'FT', 'East_Dense_Forest',
            "You are in a old farm theres lots of farming things in here", None, Seeds)

Tar_Pit = Room("Tar Pit", 'WastelandE', 'RevineE', None, 'FT',
               "Your at a tar pit a bit away from the tar river, you see something sticking out of the pit", None,
               MTP2)

RevineE = Room("Cave", 'Tar_Pit', 'WDen', None, None,
               "You walk up to the mountain side and you see an enteace to a cave, "
               "it has light coming out and you can walk into it.", None)

WDen = Room("Wyvern Cave", 'RavineE', None, 'WNest', None,
            "You reach the end of the entrance and you are surrounded by wyverns.", None)

WNest = Room("Wyvern Nest", None, None, None, 'WDen',
             "The Wyverns have let you past them and you are now in the nest", None, Pink_Egg)

WastelandE = Room("The Wasteland Entrance", 'FOW', 'Tar_Pit', None, 'Rope_Bridge',
                  "You are at the front of what looks like a run down city. The entrance is a broken fence "
                  "and you cna go in, but there is a weird fuzzy thing stuck in the fence", None,
                  Black_Bear_Skin)

FOW = Room("Evergreen Road", None, 'WastelandE', 'RTHouse', None,
           "You walk into the place and you are walking down a road..."
           "You are surrounded but 3 thieves", None)

RTHouse = Room("Rat King's house", None, None, None, 'FOW',
               "You are inside Rat King's house, You shouldn't take anything,", None)

Gates = Room("Front Gates", 'HT', 'Merchant', 'BV', 'Lawn',
             "you are at the front fo the village, "
             "you see a doctor with nurses and a big oak tree behind them to the north, "
             "a merchant to the south, and a castle far towards the east", None, Iron_Armor)

HT = Room("Doctor's Healing Tree", None, 'Gates', None, None,
          "You walk up to the area but are blocked bya nurse, the doctor "
          "comes up to you", Doctor)

Merchant = Room("Clerk's Items and More", 'Gates', None, None, None,
                "You enter the creepy Item Shop, you see many useless items"
                " sword with weird carvings", None, Merchant)

BV = Room("Back of Village", 'Blacksmith', 'Tavern', 'Kings_Castle', 'Gates',
          "You walk more in to the and see a tavern to the north, a blacksmith to the south,"
          " and the castle in the east", None)

Tavern = Room("Mute's Tavern", 'BV', None, None, None,
              "You walk into the tavern and sit at the bar, "
              "there is a bartender serving other people", None, Mute)

Blacksmith = Room("Jacks Weapons and Armory", None, 'BV', None, None,
                  "You walk up to the workshop and see a man working on "
                  "a sword", None, BlackSmith)

Kings_Castle = Room("Castle", None, None, None, 'BV', "The Room is empty but you see a hole in the floor", None)
# Players
player = Player(Spawn)
player.weapon = Dagger

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
PlayerActions = ['talk', 'take', 'drop']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print()
    if player.current_location.items is not None:
        print("There is a %s in here" % player.current_location.items.name)
    else:
        print("There is nothing in this room")

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif 'take ' in command:
        found_item = command[5:]
        _items_found = None
        if player.current_location.items is not None:
            if player.current_location.items.name.lower() == found_item.lower():
                _items_found = player.current_location.items
        if isinstance(_items_found, Item):
            print("You picked it up")
            player.inventory.append(_items_found)
            player.current_location.items = None

    elif 'drop' in command:
        lose_item = command[5:]
        _items_found = None
        for items in player.inventory:
            if items.name.lower() == lose_item.lower():
                _items_found = items

        if _items_found is not None:
            if player.current_location.items is None:
                player.current_location.items = _items_found
                player.inventory.remove(_items_found)
                print("You dropped the item %s" % _items_found.name)
            else:
                print("That item is already in there.")
        else:
            print("You don't have this item.")

    elif 'give' in command:
        give_item = command[5:]
        for items in player.inventory:
            if items.name.lower() == give_item.lower():
                give_item = items

    elif command.lower() in ["talk"]:
        for character in player.current_location:
            print(character.talk)

    elif command.lower() in ["Open Bag", "i", "Inventory"]:
        for item in player.inventory:
            print(item.name)

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
