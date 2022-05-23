command = input()
stats_dict = {}
submission = {}
while not command == "exam finished":
    command = command.split("-")
    if command[1] =="banned":
        del stats_dict[command[0]]
        command = input()
        continue
    stats_dict.setdefault(command[0],[])
    submission.setdefault(command[1],0)
    stats_dict[command[0]].extend(command[1:])
    submission[command[1]] += 1
    command = input()
else:
    print("Results:")
    [print(f"{username} | {max([int(value[points]) for points in range(len(value)) if not points %2 == 0])}") for username,value in sorted(stats_dict.items(),key = lambda x:(-int(x[1][1]),x[1][0]))]
    print("Submissions:")
    [print(f"{language} - {count}") for language,count in sorted(submission.items(),key = lambda x:(-x[1],x[0]) )]





