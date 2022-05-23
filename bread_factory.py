working_events = input().split("|")
working_events = [x.split("-") for x in working_events]

energy = 100
coins = 100


for events in range(len(working_events)):
    event_name = working_events[events][0]
    received_value = int(working_events[events][1])
    if event_name == "rest":
        gained_energy = received_value
        if energy + received_value > 100:
            gained_energy = 100 - energy

        energy += gained_energy


        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":
        earned_coins = int(working_events[events][1])
        if energy - 30 >= 0:
            energy -= 30
            coins += earned_coins
            print(f"You earned {earned_coins} coins.")
        else:
            print("You had to rest!")
            energy += 50

    else:
        ingredient = working_events[events][0]
        spend_coins = int(working_events[events][1])

        if coins - spend_coins > 0:
            print(f"You bought {ingredient}.")
            coins -= spend_coins

        else:
            print(f"Closed! Cannot afford {ingredient}.")
            break

else:
    print("Day completed!"),print(f"Coins: {coins}"),print(f"Energy: {energy}")

