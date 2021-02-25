class Player(object):
    """Represents a player of the game.

    Subclasses may override the 'tick' method to provide 
    custom animations for the player's movement depending
    on their power level, etc.

    Public attributes:
    - power: Unused power-ups (float betweent 0 and 1).
    - coins: Coins found during the level (integer).
    """

    #...