command = input()

dwarf_dict = {}

while not command == "Once upon a time":
    name,color,physics = command.split(" <:> ")
    physics = int(physics)
    dwarf_dict.setdefault(color,[])
    if name  in [names for array in dwarf_dict[color] for names in array]:
        index = [x for x in range(len(dwarf_dict[color])) if dwarf_dict[color][x][0] == name][0]
        if physics > dwarf_dict[color][index][1]:
            dwarf_dict[color][index][1] = physics
    else:
        dwarf_dict[color].append([name, physics])
    command = input()
else:
    dwarf_dict = {color:value for color,value in sorted(dwarf_dict.items(),key = lambda x:(-x[1][0][1],-len(x[1])))}
    [print(f"({hat_color}) {name} <-> {physics}") for hat_color,values in dwarf_dict.items() for name,physics in values]

