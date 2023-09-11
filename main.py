while True:
    n = input("Enter the amount of player to add: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("invalid input")

big_array = []
player = 1
meet = 0
while player <= n:
    small_array = [player, meet]
    big_array.append(small_array)
    player += 1

print("")
for x in big_array:
    print(f"Player {x[0]} already met {x[1]} people.")

already_met = []


def meet(player_a, player_b):
    for x in big_array:
        if player_a == x[0]:
            for y in big_array:
                if player_b == y[0]:
                    x[1] += 1
                    y[1] += 1
                    already_met.append((player_a, player_b))
                    already_met.append((player_b, player_a))
                    print("")
                    print(f"**Each player needs to meet {n-1} players to win**")
                    print("\nScoreboard: ")
                    for z in big_array:
                        print(f"Player {z[0]} already met {z[1]} people.")


def meet_inputs():
    player_a = int(input("\nType in the 1st player to meet: "))
    player_b = int(input("\nType in the 2nd player to meet: "))
    if player_a == player_b:
        print("\nThe player cannot meet itself: ")
        meet_inputs()
    elif (player_a, player_b) in already_met:
        print("\nThey already met each other: ")
        meet_inputs()
    else:
        meet(player_a, player_b)


winner = True
while winner:
    meet_inputs()
    for z in big_array:
        if z[1] == n-1:
            print(f"\nPlayer {z[0]} wins.")
            winner = False
