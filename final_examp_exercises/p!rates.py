command = input()

treasure_dict = {}

while not command == "Sail":
    town = command.split('||')[0]
    population = int(command.split('||')[1])
    gold = int(command.split('||')[2])
    treasure_dict.setdefault(town,[0,0])
    treasure_dict[town][1] += gold
    treasure_dict[town][0] += population
    command = input()
else:
    command_events = input()
    while not command_events == "End":
        command_events = command_events.split("=>")
        if command_events[0] == "Plunder":
            town_ = command_events[1]
            people = int(command_events[2])
            gold_ = int(command_events[3])
            treasure_dict[town_][0] -=people
            treasure_dict[town_][1] -=gold_
            print(f"{town_} plundered! {gold_} gold stolen, {people} citizens killed.")
            if treasure_dict[town_][0] == 0 or treasure_dict[town_][1] == 0:
                print(f"{town_} has been wiped off the map!")
                treasure_dict.pop(town_)
        else:
            town_ = command_events[1]
            gold_ = int(command_events[2])
            if gold_ < 0:
                print("Gold added cannot be a negative number!")
            else:
                treasure_dict[town_][1] += gold_
                print(f"{gold_} gold added to the city treasury. {town_} now has {treasure_dict[town_][1]} gold.")
        command_events = input()
    else:
        if len(treasure_dict):
            print(f'Ahoy, Captain! There are {len(treasure_dict)} wealthy settlements to go to:')
            [print(f'{town} -> Population: {value[0]} citizens, Gold: {value[1]} kg') for town,value in sorted(treasure_dict.items(),key=lambda x:(-x[1][1],x[0]))]
        else:
            print("Ahoy, Captain! All targets have been plundered and destroyed!")