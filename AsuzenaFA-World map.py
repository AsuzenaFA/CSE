world_map = {
    'SPAWN': {
        'NAME': "Your cabin",
        'DESCRIPTION': "You are in your house with your backpack on "
                       "it has two exits one to the east and one to the west",
        'PATHS': {
            'EAST': "BACKYARD",
            'WEST': "LAWN"
        }
    },
    'BACKYARD': {
        'NAME': "Your backyard",
        'DESCRIPTION': "You look around and there is an axe in a log and there is"
                       " forest to the west, north, and a water fountain to the south.",
        'PATHS' : {
            'EAST': "SPAWN",
            'WEST': "WEST_FOREST",
            'NORTH': "NORTH_FOREST",
            'SOUTH': "WATER_FOUNTAIN"

        }
    },
    'FRONTYARD': {
        'NAME': "Your lawn",
        'DESCRIPTION': "You look around and see "
    }
}