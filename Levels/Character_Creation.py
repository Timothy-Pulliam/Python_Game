from Player import Player

def character_creation():
    print("???: ...")
    print("???: Are you awake?")
    print("???: You have been out for a long time.")
    name = input("???: What is your name?\n")
    player1 = Player(name=name)
    print("???: Hello " + player1.get_name())
    print("You have 20 available stat points. You can distribute them between strength, defense, intelligence.")

    available_stats = 20
    done = False
    while not done:
        strength = int(input("How strong are you? (%s/20 stat points left)" % available_stats))
        while strength > available_stats:
            print("Not enough stat points")
            strength = int(input("How strong are you? (%s/20 stat points left)" % available_stats))
        available_stats -= strength
        defense = int(input("How tough are you? (%s/20 stat points left)" % available_stats))
        while defense > available_stats:
            print("Not enough stat points")
            defense = int(input("How tough are you? (%s/20 stat points left)" % available_stats))
        available_stats -= defense
        intelligence = int(input("How wise are you? (%s/20 stat points left)" % available_stats))
        while intelligence > available_stats:
            print("Not enough stat points")
            intelligence = int(input("How wise are you? (%s/20 stat points left)" % available_stats))
        available_stats -= intelligence

        player1.set_stat('strength', strength)
        player1.set_stat('defense', defense)
        player1.set_stat('intelligence', intelligence)

        print("Are the following stats correct?")
        print(stats)
        response = input()
        if response.lower() == 'y' or response.lower() == 'yes':
            done = True
        else:
            #stats = {'strength': 0, 'defense': 0, 'intelligence': 0}
            available_stats = 20

    print("Character Created. Stats printed below")
    print(stats)
    print("Okay. Great. I see you are a strong person.")
