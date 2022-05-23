command = input()

stats_dict = {}
unlike_count = 0
while not command == "Stop":
    command = command.split("-")
    if command[0] =="Like":
        stats_dict.setdefault(command[1],[])
        if command[2] not in [x for x in stats_dict[command[1]]]:
            stats_dict[command[1]].append(command[2])
    elif command[0] == "Unlike":
        if command[1] not in stats_dict:
            print(f"{command[1]} is not at the party.")
        elif command[2] in stats_dict[command[1]]:
            stats_dict[command[1]].remove(command[2])
            unlike_count += 1
            print(f"{command[1]} doesn't like the {command[2]}.")
        elif command[2] not in stats_dict[command[1]]:
            print(f"{command[1]} doesn't have the {command[2]} in his/her collection.")
    command = input()
else:
    for name,meal in sorted(stats_dict.items(),key = lambda x:(-len(x[1]),x[0])):
        print(f"{name}: ",end="")
        print(*[x for x in meal],sep=', ')
    print(f"Unliked meals: {unlike_count}\n")


