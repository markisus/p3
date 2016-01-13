"""
locations of player data in RAM
will generate a list of all locations in the Locations.txt
format required by Dolphin when run as standalone script
"""

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

def generate_locations_for_player(player_index):
    locations = []
    player_block_start = PLAYER_ONE_BLOCK_START + player_index * PLAYER_BLOCK_INCREMENT
    character_data_pointer = player_block_start + PLAYER_CHARACTER_DATA_POINTER
    
    locations.append(("x_position", "{:x}".format(player_block_start + PLAYER_X_POSITION)))
    locations.append(("y_position", "{:x}".format(player_block_start + PLAYER_Y_POSITION)))
    locations.append(("percentage", "{:x}".format(player_block_start + PLAYER_PERCENTAGE)))
    locations.append(("stocks", "{:x}".format(player_block_start + PLAYER_STOCKS)))
    locations.append(("in_air", "{:x} {:x}".format(character_data_pointer, PLAYER_CHARACTER_GROUND_AIR_STATE)))

    return locations

def generate_lookup():
    """
    returns a dict keyed on the memory address
    whose value is a tuple of (player, location_name)
    """
    lookup = {}
    for i in range(4):
        for location_name, location in generate_locations_for_player(i):
            lookup[location] = (i, location_name)
    return lookup

if __name__ == "__main__":
    for i in range(4):
        locations = generate_locations_for_player(i)
        for location_name, location in locations:
            print(location)
