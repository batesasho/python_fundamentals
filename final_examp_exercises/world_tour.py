text_all_stops = input()
initial_text = text_all_stops
command = input()

while not command == "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        if int(command[1]) in range(len(text_all_stops)):
            text_all_stops = text_all_stops[:int(command[1])] + command[2]+text_all_stops[int(command[1]):]

    elif command[0] == "Remove Stop":
        if (int(command[1]) in range(len(text_all_stops))) and (int(command[2]) in range(len(text_all_stops))):
            text_all_stops = text_all_stops[:int(command[1])] + text_all_stops[int(command[2])+1:]

    elif command[0] == "Switch":
        if command[1] in initial_text:
            text_all_stops = text_all_stops.replace(command[1],command[2])
    print(text_all_stops)


    command = input()
else:
    print(f"Ready for world tour! Planned stops: {text_all_stops}")