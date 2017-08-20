import numpy
# Constants
TERRAIN_TYPES = {'grass': None, 'water': None, 'fire': None, 'ice': None}

class Node(object):

    # Can the player walk onto this node?
    accessible = False
    # Any hidden items on this node?
    items = []
    # Any special dialogue associated with this node?
    dialogue = ""
    # Different Terrain types have different effects on the player's stats and gameplay.
    # The default terrain type is grass
    terrain = 'grass'

    def __init__(self, accessible=False, items=[], dialogue="", terrain='grass'):
        self.accessible = accessible
        self.items = items
        self.dialogue = dialogue
        self.terrain = terrain

    def set_accessible(self):
        self.accessible = True

    def set_inaccessible(self):
        self.accessible = False

    def get_accessible(self):
        return self.accessible

    def set_items(self, *items):
        """Populates a node with a list of items. Useful for creating treasure chests, etc. Players can inspect Nodes to find items."""
        self.items = [item for item in items]

    def get_items(self):
        """Return the list of items this Node contains. Players can inspect Nodes to find items."""
        return self.items

    def set_dialogue(self, dialogue_text):
        assert isinstance(dialogue_text, str), "Node Object set_dialogue method dialogue_text argument is not of type <str>"
        self.dialogue = dialogue_text

    def get_dialogue(self):
        return self.dialogue

    def set_terrain(self, new_terrain):
        assert new_terrain in TERRAIN_TYPES.keys(), "Node Object set_terrain method new_terrain argument not a valid TERRAIN_TYPE"
        self.terrain = new_terrain



def generate_map(n, m):
    """Generates a map. Map is a 2-D array (numpy matrix) with dimensions nxm
    n = height
    m = width
    """
    print numpy.zeros((n, m))
    return numpy.zeros((n, m))

if __name__ == '__main__':
    generate_map(5,5)
