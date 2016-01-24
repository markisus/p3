import memory_map

class PlayerState:
    def __init__(self, player_index):
        self.player_index = player_index
        self.in_air = False
        self.x_position = 0.0;
        self.y_position = 0.0;

    def __str__(self):
        return \
            """player_index {}
            in_air {}
            x_position {}
            y_position {}
            """.format(
                self.player_index,
                self.in_air,
                self.x_position,
                self.y_position)
    
class GameState:
    def __init__(self):
        self.players = [
            PlayerState(player_index) for player_index in range(4)
        ]
        self.lookup = memory_map.generate_lookup()

    def update(self, address, value):
        if address in self.lookup:
            player_index, variable = self.lookup[address]
            player = self.players[player_index]

            
            setattr(
                player,
                variable.name,
                variable.type.parse_bytes(value)
            )
        else:
            print("address {} not found".format(address))

    def __str__(self):
        return "\n".join((str(player) for player in self.players))
