command = input()
judge_dict = {}


while not command == "no more time":
    user_name,contest,points = command.split(" -> ")
    points = int(points)
    judge_dict.setdefault(contest,{user_name:points})

    if user_name in judge_dict[contest]:
        if points > judge_dict[contest][user_name]:
            judge_dict[contest].update({user_name:points})
    else:
        judge_dict[contest][user_name] = points

    command = input()

else:
    individual_stats = {}

    for key,value in judge_dict.items():
        print(f'{key}: {len(value)} participants')
        position = 1
        for name,points in sorted(value.items(),key=lambda x:(-x[1],x[0])):
            print(f'{position}. {name} <::> {points}')
            position += 1

    for stats in judge_dict.values():
        for name,point in stats.items():
            individual_stats.setdefault(name,0)
            individual_stats[name] += point

    print("Individual standings:")
    i = 1
    for names,points in sorted(individual_stats.items(),key=lambda x: (-x[1],x[0])):
        print(f'{i}. {names} -> {points}')
        i += 1

