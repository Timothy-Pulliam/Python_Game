from Player import Player

def main():

    player_name = input("What is your character's name?\n")
    player1 = Player(name=player_name, stats={'max_health':20, 'current_health':20, 'strength':1, })
    print(player1.get_name())
    print(player1.get_stats())

if __name__ == '__main__':
    main()
