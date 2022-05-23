command_one = input()
contest_dic = {}

max_points = 0
name_winner = ""
while not command_one == "end of contests":
    contest = command_one.split(":")[0]
    password_cont = command_one.split(":")[1]
    contest_dic.setdefault(contest)
    contest_dic[contest] = (password_cont)
    command_one = input()

command_two = input()
submission_dic = {}
while not command_two == "end of submissions":
    cont, password, user_name, points = command_two.split("=>")
    if cont in contest_dic and password == contest_dic[cont]:
        submission_dic.setdefault(user_name, {cont:int(points)})
        if  (cont in submission_dic[user_name]):
            if (int(points) > submission_dic[user_name][cont]):
                submission_dic[user_name].update({cont: int(points)})
        else:
            submission_dic[user_name][cont] = int(points)
    command_two = input()
else:
    for name,value in submission_dic.items():
        total_points = 0
        for el in value:
            total_points += value[el]
        if total_points > max_points:
            max_points = total_points
            name_winner = name
    print(f"Best candidate is {name_winner} with total {max_points} points.")
    print("Ranking:")
    for names,val in sorted(submission_dic.items(),key = lambda x:x[0]):
        print(f"{names}")
        for el_,values in sorted(val.items(),key=lambda x:-x[1]):
            print(f"#  {el_} -> {val[el_]}")
