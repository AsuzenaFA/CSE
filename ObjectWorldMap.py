class Room(object):
    def __init__(self, name, north, south, east, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


Spawn = Room("Your Cabin", None, None, 'Backyard', 'Lawn',
             "You are in your house with your backpack on "
             "it has two exits one to the east and one to the west")

Backyard = Room("Your backyard", 'North_Forest', 'Water_Fountain', 'Spawn', 'West_Forest',
                "You look around and there is an axe in a log and there is"
                " forest to the west, north, and a water fountain to the south.")

NF = Room("Northern Forest", 'Grass Trail', 'Gates', 'Tar_Rivers', 'Desert',
          "Your in a quiet forest and you hear grass hoppers to the north")

WF = Room("Western Forest", '')

EF = Room("Eastern Forest",)

SF = Room("Southern Forest",)

Lawn = Room("Your Lawn", 'North_Forest', 'Water_Fountain', 'Gates', 'Spawn',
            "You look around and see the water fountain to the south, forest to the north,and a big wooden"
            "gate to the east.")

Water_Fountain = Room("Broken Water Fountain", 'Spawn', 'Swamp', 'East_Forest', 'West_Forest',
                      "The fountain seems to be broken. You look around to see forest to the south, west, and east")



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

