from Player import Player

def character_creation():
    print("...")
    print("Are you awake?")
    print("You have been out for a long time.")
    name = input("What is your name?\n")

    player1 = Player(name=name)
    print("Hello " + player1.get_name())

    available_stat_points = 20
    print("You have 20 stats points. How do you want to spend them?")
    done = False

    while (not done) and available_stat_points > 0:
        strength = int(input("How strong are you? (%s/20 available stat points) " % available_stat_points))
        available_stat_points -= strength
        defense = int(input("How much can you endure? (%s/20 available stat points) " % available_stat_points))
        available_stat_points -= defense
        intelligence = int(input("Are you good with magic? (%s/20 available stat points) " % available_stat_points))
        available_stat_points -= intelligence

        player1.set_stat('strength', strength)
        player1.set_stat('defense', defense)
        player1.set_stat('intelligence', intelligence)

        print("Are these stats correct?")
        player1.get_stats()
        response = input()
        if response.lower() == 'y' or response.lower() == 'yes':
            done = True

    print("Okay. Great. I see you are a strong person.")
