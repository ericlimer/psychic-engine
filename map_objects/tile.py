

class Tile:
# tiles on the map, may or may not be passible/block sight
    def __init__(self, blocked, blocks_sight=None):
        self.blocked = blocked

        if blocks_sight is None:
            blocks_sight = blocked
    
        self.blocks_sight = blocks_sight