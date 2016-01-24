"""
locations of player data in RAM
will generate a list of all locations in the Locations.txt
format required by Dolphin when run as standalone script
"""

from collections import namedtuple
from variable import Variable, VariableType

# Static player block
PLAYER_BLOCK_INCREMENT = 0xE90
PLAYER_ONE_BLOCK_START = 0x80453080
PLAYER_X_POSITION = 0x10
PLAYER_Y_POSITION = 0x14
PLAYER_PERCENTAGE = 0x60
PLAYER_STOCKS = 0x8E

# Character data
PLAYER_CHARACTER_DATA_POINTER = 0xB0
PLAYER_CHARACTER_GROUND_AIR_STATE = 0x140

# Variables
X_POSITION = Variable('x_position', VariableType.Float)
Y_POSITION = Variable('y_position', VariableType.Float)
STOCKS = Variable('stocks', VariableType.Int)
PERCENTAGE = Variable('percentage', VariableType.Float)
IN_AIR = Variable('in_air', VariableType.Bool)

def generate_locations_for_player(player_index):
    """
    returns a list of (variable, string) tuples
    for player_index, where the variable names the
    field and type, and string names the location in memory
    """
    locations = []
    player_block_start = PLAYER_ONE_BLOCK_START + player_index * PLAYER_BLOCK_INCREMENT
    character_data_pointer = player_block_start + PLAYER_CHARACTER_DATA_POINTER
    
    locations.append((X_POSITION, "{:x}".format(player_block_start + PLAYER_X_POSITION)))
    locations.append((Y_POSITION, "{:x}".format(player_block_start + PLAYER_Y_POSITION)))
    locations.append((PERCENTAGE, "{:x}".format(player_block_start + PLAYER_PERCENTAGE)))
    locations.append((STOCKS, "{:x}".format(player_block_start + PLAYER_STOCKS)))
    locations.append((IN_AIR, "{:x} {:x}".format(character_data_pointer, PLAYER_CHARACTER_GROUND_AIR_STATE)))

    return locations

def generate_lookup():
    """
    returns a dict keyed on the memory address
    whose value is a tuple of (player_index, variable)
    """
    lookup = {}
    for i in range(4):
        for variable, location in generate_locations_for_player(i):
            lookup[location] = (i, variable)
    return lookup

if __name__ == "__main__":
    for i in range(4):
        locations = generate_locations_for_player(i)
        for variable, location in locations:
            print(location)
