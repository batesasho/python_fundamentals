text = input()
command = input()

while not command == "Decode":
    command=command.split("|")
    if command[0] == "Move":
        text = text[int(command[1]):] + text[:int(command[1])]
    elif command[0] == "Insert":
        text = text[:int(command[1])] + command[2] + text[int(command[1]):]
    elif command[0] == "ChangeAll":
        text=text.replace(command[1],command[2])
    command = input()
else:
    print(f"The decrypted message is: {text}")