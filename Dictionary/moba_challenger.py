command = input()
player_pool_dict = {}

while not command == "Season end":
    if " -> " in command:
        name_player, position, skills = command.split(" -> ")
        skills = int(skills)
        player_pool_dict.setdefault(name_player,{position:skills})
        if name_player in player_pool_dict[name_player]:
            if skills > player_pool_dict[name_player][position]:
                player_pool_dict[name_player].update({position:skills})
        else:
            player_pool_dict[name_player][position] = skills # checked whether could be done with

    else:
        player_one,player_two = command.split(" vs ")
        if player_one in player_pool_dict and player_two in player_pool_dict:
            for common_position,points in player_pool_dict[name_player].items():
                if common_position in player_pool_dict[player_one] and common_position in player_pool_dict[player_two]:
                    if sum(player_pool_dict[player_one].values()) > sum(player_pool_dict[player_two].values()):
                        del player_pool_dict[player_two] # to be checked whether the key is removed only or the entire Key:value
                    elif sum(player_pool_dict[player_one].values()) < sum(player_pool_dict[player_two].values()):
                        del player_pool_dict[player_one]

    command = input()
else:
    #total_sum_dic = {name:sum(total_value.values()) for name,total_value in player_pool_dict.items() }

    for name,value in sorted(player_pool_dict.items(),key = lambda x:(-sum(x[1].values()), x[0])):
        print(f"{name}: {sum(value.values())} skill")
        [print(f"- {position} <::> {skill}") for position,skill in sorted(value.items(),key = lambda x:(-x[1],x[0]))]