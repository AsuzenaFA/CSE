
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

player = Player(Spawn)
player.weapon = Dagger

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
PlayerActions = ['give', 'talk', 'pick up', 'drop']
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
