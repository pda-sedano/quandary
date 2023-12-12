class Player:
    """
    Implements a player of the CHSH game.
    """

    def __init__(self, game_manager):
        self.game_manager = game_manager

    def add_measurement(self, theta):
        self.game_manager.quantum_circuit.ry(theta, self.player_index)

    def send_response_bit(self, bit):
        self.game_manager.response_bit[self.player_index] = bit

