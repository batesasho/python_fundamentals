import re
number = int(input())


plant_dict = {}
for i in range(number):
    plant_info = input().split("<->")
    plant_dict.setdefault(plant_info[0],[0])
    plant_dict[plant_info[0]][0] += int(plant_info[1])
else:

    command = input()
    while not command == "Exhibition":
        command = command.replace(" ","")
        command = re.split(r'[:-]',command)
        if command[1] in plant_dict:
            if command[0] == "Rate":
                plant_dict[command[1]].append(int(command[2]))
            elif command[0] == "Update":
                plant_dict[command[1]][0] = int(command[2])
            elif command[0] == "Reset":
                plant_dict[command[1]] = plant_dict[command[1]][:1]
        else:
            print("error")
        command = input()
    else:

        for key,value in plant_dict.items():
            sum_ = 0
            sum_average = 0
            if len(value) > 1:
                for el in range(1,len(value)):
                    sum_ += int(value[el])
                sum_average = float(sum_/(len(value)-1))
            plant_dict[key] = [value[0],sum_average]
        print("Plants for the exhibition:")
        [print(f'- {plant_name}; Rarity: {value[0]}; Rating: {value[1]:.2f}') for plant_name,value in sorted(plant_dict.items(),key = lambda x:(-x[1][0],-x[1][1]))]