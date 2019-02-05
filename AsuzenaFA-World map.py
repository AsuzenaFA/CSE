world_map = {
    'SPAWN': {
        'NAME': "Your cabin",
        'DESCRIPTION': "You are in your house with your backpack on "
                       "it has two exits one to the east and one to the west",
        'PATHS': {
            'EAST': "BACKYARD",
            'WEST': "LAWN"
            # DOWN : CLOSET
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
        'DESCRIPTION': "You enter and you are at the front fo the village, "
                       "you see a doctor with nurses and a big oak tree behind them to the north, "
                       "a merchant to the south, and a castle far towards the east",
        'PATHS': {
            'EAST': 'BACK_VILLAGE',
            'NORTH': 'HEALING_TREE',
            'SOUTH': 'MERCHANT'
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
    }