world_map = {
    'SPAWN': {
        'NAME': "Your cabin",
        'DESCRIPTION': "You are in your house with your backpack on "
                       "it has two exits one to the east and one to the west",
        'PATHS': {
            'EAST': 'BACKYARD',
            'WEST': 'LAWN',
            # DOWN : BASEMENT
        }
    },
    'BACKYARD': {
        'NAME': "Your backyard",
        'DESCRIPTION': "You look around and there is an axe in a log and there is"
                       " forest to the west, north, and a water fountain to the south.",
        'PATHS': {
            'EAST': "SPAWN",
            'WEST': "WEST_FOREST",
            'NORTH': "NORTH_FOREST",
            'SOUTH': "WATER_FOUNTAIN"

        }
    },
    'WEST_FOREST': {
        'NAME': "Western Forest",
        'DESCRIPTION': "As you are going through the Northern Forest you come across large black egg and its moving"
                       ", what do you do"
    },
    'WATER_FOUNTAIN': {
        'NAME': "Broken Water Fountain",
        "DESCRIPTION": "The fountain seems to be broken. You look around to see forest to the south, west, and east",
        'PATHS': {
            'NORTH': "SPAWN",
            'WEST': "WEST_FOREST",
            'SOUTH': "SWAMP",
            'EAST': "TAR_RIVER"
        }
    },
    'TAR_RIVER': {
        'NAME': "Tar River",
        "DESCRIPTION": "You go through the Eastern Forest and come across a Tar River, You look around"
                       " and see a bridge to the north and a fallen tree to the south.",
        'PATHS': {
            'NORTH': "BROKEN_BRIDGE",
            'SOUTH': "FALLEN_TREE",
            'WEST': "WATER_FOUNTAIN"
        }
    },
    'FALLEN_TREE': {
        'NAME': "Fallen Tree",
        "DESCRIPTION": "You see a fallen tree that goes over the tar river and you smoke coming out of the ground"
                       " towards the east.",
        'PATHS': {
            'EAST': "RAVIEN"
        }
    },
    'SWAMP': {
        'NAMES': "Swamp Lands",
        'DESCPRIPTION': "Your in a foggy swamp area and it looks like no one is around.",
        'PATHS': {
            'NORTH': "WATER_FOUNTAIN",
            'SOUTH': "OGRE_CLAN",
            'WEST': "DENSE_FOREST",
            'EAST': "POND"
        }
    },
    'POND': {
        'NAME': "Pond",
        'DESCRIPTION': "You look into the pond and see many colorful Koi Fish, but you see one that's very big and"
                       " fully golden",
        'PATHS': {
            'NORTH': "WATER_FOUNTAIN",
            'SOUTH': "OGRE_CLAN",
            'WEST': "SWAMP",
            'EAST': "FALLEN_TREE"
        }
    },
    'OGRE_CLAN': {
        'NAME': "Ogre Village",
        'DESCRIPTION': ""
    },
   
    'FRONTYARD': {
        'NAME': "Your lawn",
        'DESCRIPTION': "You look around and see the water fountain to the south, forest to the north,and a big wooden"
                       "gate to the east.",
        'PATHS': {
            'EAST': "GATES",
            'WEST': "SPAWN",
            'NORTH': "NORTH_FOREST",
            'SOUTH': "WATER_FOUNTAIN"
        }
    },
    'GATES': {
        'NAME': "Wooden Gates",
        'DESCRIPTION': "you are at the front fo the village, "
                       "you see a doctor with nurses and a big oak tree behind them to the north, "
                       "a merchant to the south, and a castle far towards the east",
        'PATHS': {
            'EAST': "BACK_VILLAGE",
            'NORTH': "HEALING_TREE",
            'SOUTH': "MERCHANT"
        }
    },
    'HEALING_TREE': {
        'NAME': "Doctors",
        'DESCRIPTION': "You walk up to the area but are blocked by a nurse, the doctor " 
                       "comes up to you and says you need to pay to get by the fence",
        'PATHS': {
            'SOUTH': "GATES"
        }
    },
    'MERCHANT': {
        'NAME': "Item Shop",
        'DESCRIPTION': "You enter the creepy Item Shop, you see many useless items but then see an elephant tusk"
                       " sword with weird carvings",
        'PATHS': {
            'NORTH': "GATES"
        }

    },
    'BACK_VILLAGE': {
        'NAME': "Back Of Village",
        'DESCRIPTION': "You walk more in to the and see a tavern to the north, a blacksmith to the south,"
                       " and the castle in the east",
        'PATHS': {
            'EAST': "KINGS_CASTLE",
            'SOUTH': "TAVERN",
            'NORTH': "BLACKSMITH",

        }
    },
    'TAVERN': {
        'NAME': "Mute's Tavern",
        'DESCRIPTION': "You walk into the tavern and sit at the bar, "
                       "there is a bartender serving other people",
        'PATHS': {
            'SOUTH': "BACK_VILLAGE"
            # 'DOWN': "M_BASEMENT"
        }
    },
    'BLACKSMITH': {
        'NAME': "Armory and Weapons Workshop",
        'DESCRIPTION': "You walk up to the workshop and see a man working on "
                       "a sword",
        'PATHS': {
            'NORTH': "BACK_VILLAGE"
        }
    },
    'CASTLE': {
        'NAME': "Kings Castle",
        'DESCRIPTION': "The Room is empty but you see a hole in the floor",
        'PATHS': {
            'DOWN': "BATTLE GROUND",
            'WEST': "BACK_VILLAGE"
        }
    },

}
current_node = world_map['SPAWN']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True


while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized")
