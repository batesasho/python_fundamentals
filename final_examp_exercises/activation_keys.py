activation_key = input()
command = input().split(">>>")


while not command[0] == "Generate":

    if command[0] == "Contains":
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        if command[1] == "Upper":
            upper_case = activation_key[int(command[2]):int(command[3])]
            activation_key = activation_key.replace(upper_case, upper_case.upper())

        else:
            lower_case = activation_key[int(command[2]):int(command[3])]
            activation_key  = activation_key.replace(lower_case, lower_case.lower())
        print(activation_key)
    elif command[0] == "Slice":
        activation_key = activation_key[:int(command[1])] + activation_key[int(command[2]):]
        print(activation_key)

    command = input().split(">>>")
else:
    print(f"Your activation key is: {activation_key}")