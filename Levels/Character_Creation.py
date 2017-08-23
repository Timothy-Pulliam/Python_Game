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
        while 0 > strength or strength > available_stats:
            print("Not enough stat points")
            strength = int(input("How strong are you? (%s/20 stat points left)" % available_stats))
        available_stats -= strength

        defense = int(input("How tough are you? (%s/20 stat points left)" % available_stats))
        while 0 > defense or defense > available_stats:
            print("Not enough stat points")
            defense = int(input("How tough are you? (%s/20 stat points left)" % available_stats))
        available_stats -= defense

        intelligence = int(input("Are you good with magic? (%s/20 stat points left)" % available_stats))
        while 0 > intelligence or intelligence > available_stats:
            print("Not enough stat points")
            intelligence = int(input("Are you good with magic? (%s/20 stat points left)" % available_stats))
        available_stats -= intelligence

        constitution = int(input("Is your mind strong?? (%s/20 stat points left)" % available_stats))
        while 0 > constitution or constitution > available_stats:
            print("Not enough stat points")
            constitution = int(input("Is your mind strong? (%s/20 stat points left)" % available_stats))
        available_stats -= constitution

        speed = int(input("How fast are you? (%s/20 stat points left)" % available_stats))
        while 0 > speed or speed > available_stats:
            print("Not enough stat points")
            speed = int(input("How fast are you? (%s/20 stat points left)" % available_stats))
        available_stats -= speed

        player1.set_stats(max_health=20, current_health=20,
                          max_mana=10, current_mana=10,
                          strength=strength, defense=defense,
                          intelligence=intelligence, constitution=constitution,
                          speed=speed)
        print("Are the following stats correct?")
        print(player1.get_stats())
        response = input()
        if response.lower() == 'y' or response.lower() == 'yes':
            done = True
        else:
            player1.set_stats()
            available_stats = 20

    print("Character Created. Stats printed below")
    print(player1.get_stats())
    print("Okay. Great. I see you are a strong person.")
