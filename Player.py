class Player(object):

    name = ''
    stats = {
             'max_health' : 0,       # When current_health drops to 0, player dies. current_health cannot exceed max_health.
             'current_health' : 0,
             'max_mana' : 0,         # When current_mana drops to 0, player can no longer cast spells. current_mana cannot exceed max_mana.
             'current_mana' : 0,
             'strength' : 0,         # How much physical damage you inflict
             'defense' : 0,          # How much you resist physical damage
             'intelligence' : 0,     # How much magic damage you inflict
             'constitution' : 0,     # How much you resist magic damage
             'speed' : 0,            # speed effects the likelyhood of critical hits as well as turn order
             }
    # Inventory is populated by items from the Item class (Item.py)
    inventory = []
    # Money is needed to buy items from shops
    money = 0
    # Each time you level up, your stats increase in accordence to your player's character class
    level = 0
    # You need experience to level up
    experience = 0

    def set_name(self, name):
        assert isinstance(name, str), "Player Object set_name method name argument is not of type <str>"
        self.name = name

    def get_name(self):
        return self.name

    def set_max_health(self, max_health):
        self.max_health = max_health

    def get_max_health(self):
        return self.max_health

    def set_current_health(self, current_health):
        self.current_health = current_health

    def get_curren_health(self):
        return self.current_health

    def set_max_mana(self, max_mana):
        self.max_mana = max_mana

    def get_max_mana(self):
        return self.max_mana

    def set_current_mana(self, current_mana):
        self.current_mana = current_mana

    def get_current_mana(self):
        return self.current_mana

    def set_strength(self, strength):
        self.strength = strength

    def

    def
