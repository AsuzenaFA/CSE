import Items
import Characters
import Player


class Room(object):
    def __init__(self, name, north, south, east, west, description, items=[], shop=None, character=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.shop = shop
        self.description = description
        self.character = character
        self.items = items


Spawn = Room("Your Cabin", None, None, 'Lawn', 'Backyard',
             "You are in your house with your backpack on "
             "it has two exits one to the east and one to the west", [LongSword])

Backyard = Room("Your backyard", 'North_Forest', 'Water_Fountain', 'West_Forest', 'Spawn',
                "You look around and there is a hatchet in a log and there is"
                " forest to the west, north, and a water fountain to the south.", [Hatchet])

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
          "to the south the you cant climb", [BattleAxe])

Tar_Pit = Room("Tar Pit", 'Wasteland', 'Revine', None, 'FT',
               "Your at a tar pit a bit away from the tar river, you see something sticking out of the pit",
               [MTP2])

Revine = Room("Wyvern's Cave", 'Tar_Pit', None, None, None,
              "You wonder into a revine, its very hot, you see a sliver "
              "of light in the wall and you walk towards it..."
              "When you reach the other side you are surrounded by wyverns", [PinkEgg])

WastelandE = Room("The Wasteland Entrance", 'FOW', 'Tar_Pit', None, 'Rope_Bridge',
                  "You are at the front of what looks like a run down city. The entence is a broken fence "
                  "and you cna go in, but there is a weird fuzzy thing stuck in the fence", [BlackBearSkin])

FOW = Room("Evergreen Road", 'MOW', 'WastelandE', None, None,
           "You walk into the place and you are walking down a road..."
           "You are surrounded but 3 thieves", [], None,)

Gates = Room("Front Gates", 'HT', 'Merchant', 'BV', 'Lawn',
             "you are at the front fo the village, "
             "you see a doctor with nurses and a big oak tree behind them to the north, "
             "a merchant to the south, and a castle far towards the east")

HT = Room("Doctor's Healing Tree", None, 'Gates', None, None,
          "You walk up to the area but are blocked by a nurse, the doctor "
          "comes up to you", [BigHealth, SmallHealth], DoctorsHT, Doctor)

Merchant = Room("Clerk's Items and More", 'Gates', None, None, None,
                "You enter the creepy Item Shop, you see many useless items but then see an elephant tusk"
                " sword with weird carvings", [BigHealth, BigStamina, BigMana, SmallHealth, SmallMana, SmallStamina,
                                               MTP1], Merchant, MerchantsShop)

BV = Room("Back of Village", 'Blacksmith', 'Tavern', 'Kings_Castle', None,
          "You walk more in to the and see a tavern to the north, a blacksmith to the south,"
          " and the castle in the east")

Tavern = Room("Mute's Tavern", None, BV, None, None,
              "You walk into the tavern and sit at the bar, "
              "there is a bartender serving other people", [], Mute, MutesTavern)

Blacksmith = Room("Jacks Weapons and Armory", None, 'BV', None, None,
                  "You walk up to the workshop and see a man working on "
                  "a sword", [], BlackSmith, BlacksmithShop)

Kings_Castle = Room("Castle", None, None, None, 'BV', "The Room is empty but you see a hole in the floor")

