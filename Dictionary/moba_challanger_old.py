command = input()

stats_dic = {}

while not command == "Season end":
    if " -> " in command:
        name, position, skills = command.split(" -> ")
        skills = int(skills)
        stats_dic.setdefault(name,{position:skills})
        if position in stats_dic[name]:
            if skills > stats_dic[name][position]:
                stats_dic[name].update({position:skills})
        else:
            stats_dic[name][position] = skills
    elif " vs " in command:
        first_player, second_player = command.split(" vs ")
        if first_player in stats_dic and second_player in stats_dic:
            for position,point in stats_dic[first_player].items():
                if position in stats_dic[second_player]:
                    if point > stats_dic[second_player][position]:
                        del stats_dic[second_player]
                        break
                    else:
                        del stats_dic[first_player]
                        break
    command = input()

else:
    dic_skill = {}
    dic_skill = {name_:sum(skill_.values()) for name_,skill_ in stats_dic.items() }
    for key,value in sorted(dic_skill.items(),key = lambda x:(-x[1],x[0])):
        print(f"{key}: {value} skill")
        [print(f"- {k} <::> {v}") for k,v in sorted(stats_dic[key].items(),key=lambda x:(-x[1],x[0]))]

