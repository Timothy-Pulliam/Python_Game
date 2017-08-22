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

    def get_stats(self, *stats):
        """Returns the numerical value of the stats passed to the method as a Python dictionary. For example:
        If you want to know the player's max_health and defense, you would invoke as follows:

        Player.get_stats('max_health', 'defense')

        If you want to return all of the user's stats, you can simply invoke as follows:

        Player.get_stats()
        """
        for stat in stats:
            assert stat in self.stats.keys(), "Player.get_stat(): Player stat " + str(stat) + " is not a valid player stat"
        if len(stats) == 0:
            return self.stats
        else:
            return {s: self.stats[s] for s in stats}

    def set_stats(self, **stats):
        """The way player stats are set during character creation.

        For example, to set all player stats to 0:
        Player.set_stats()

        To set each stat individually:
        Player.set_stats('max_health'=20, 'current_health'=20, 'defense'=10, 'strength'=12)

        """

        for key in stats.keys():
            assert key in self.stats.keys(), "Player.set_stat(): Player stat " + str(stat) + " is not a valid player stat"
        if len(stats) == 0:
            for key in self.stats.keys():
                self.stats[key] = 0
        else:
            for key, value in stats.items():
                self.stats[key] = value

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
