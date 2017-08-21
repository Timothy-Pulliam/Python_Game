class Player(object):

    # CLASS VARIABLES (shared by all instances)

    # TODO Fix this constructor
    def __init__(self, name='', stats={
                                'max_health' : 0,       # When current_health drops to 0, player dies. current_health cannot exceed max_health.
                                'current_health' : 0,
                                'max_mana' : 0,         # When current_mana drops to 0, player can no longer cast spells. current_mana cannot exceed max_mana.
                                'current_mana' : 0,
                                 'strength' : 0,        # How much physical damage you inflict
                                'defense' : 0,          # How much you resist physical damage
                                'intelligence' : 0,     # How much magic damage you inflict
                                'constitution' : 0,     # How much you resist magic damage
                                'speed' : 0,            # speed effects the likelyhood of critical hits as well as turn order
                                       }):

        # INSTANCE VARIABLES (only used by one instance)
        self.name = name
        self.stats = stats
        # Inventory is populated by items from the Item class (Item.py)
        self.inventory = []
        # Money is needed to buy items from shops
        self.money = 0
        # Each time you level up, your stats increase in accordence to your player's character class
        self.level = 0
        # You need experience to level up
        self.experience = 0

    def set_name(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def get_stats(self):
        """Return all stats"""
        return self.stats

    def get_stat(self, stat):
        """Returns the numerical value of the stat passed to the method. For example,
        If you want to know the player's max_health, you would invoke as follows

        Player.get_stat('max_health')
        """
        assert stat in self.stats.keys(), "Player.get_stat(): Player stat " + str(stat) + " is not a valid player stat"
        return self.stats[stat]

    def set_stat(self, stat, new_value):
        """The preffered way to change a player's stats. This could be due to status ailements, leveling, healing, etc.
        For example, suppose a player heals themselves using a potion. The set_stat() method would be invoked as follows:

        Player.set_stat('current_health', player1.get_stat('current_health') + 20)
        """

        assert stat in self.stats.keys(), "Player.set_stat(): Player stat " + str(stat) + " is not a valid player stat"
        self.stats[stat] = int(new_value)

    def get_inventory(self):
        return self.inventory

    def add_inventory_item(self, *items):
        """Suppose a player finds a treasure chest with three items. You would
        envoke this method as follows:

        Player.add_inventory_item('rock', 'potion', 'helmet')"""
        self.inventory.extend(items)

    def get_money(self):
        return self.Money

    def set_money(self, new_value):
        self.money = new_value
