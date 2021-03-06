world_map = {
    'R19A': {
        'NAME': "Mr. Weibe's Classroom",
        'DESCRIPTION': "This is the classroom that you are in right now. "
                       "It has two exits to the north side",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }

    },
    'PARKING_LOT': {
        'NAME': "The Edison Parking lot",
        'DESCRIPTION': "There are cars parked here. To"
                       " the south is Mr. Weibe's room",
        'PATHS': {
            'SOUTH': "R19A"
        }

    }
}

# Other Variable
current_node = world_map['R19A']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# Controller

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


