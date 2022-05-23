command = input()
courses_stats_dic = {}
while not command == "end":
    command = command.split(" : ")
    courses_stats_dic.setdefault(command[0],[])
    courses_stats_dic[command[0]].append(command[1])

    command = input()
else:

    for course,name in sorted(courses_stats_dic.items(),key=lambda x: -len(x[1])):
        print(f"{course}: {len(name)}")
        for n in sorted(name):
            print(f"-- {n}")

