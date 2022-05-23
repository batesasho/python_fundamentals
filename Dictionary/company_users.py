command = input()
stats_dict = {}
while not command == "End":
    command = command.split(" -> ")
    name = command[0]
    id = command[1]
    stats_dict.setdefault(name,[])
    if id not in stats_dict[name]:
        stats_dict[name].append(id)
    command = input()
else:
    for name,id in sorted(stats_dict.items(),key = lambda x:x[0]):
        print(f"{name}")
        for n in id:
            print(f"-- {n}")