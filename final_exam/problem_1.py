text = input()
command = input()


while not command == "Done":
    command = command.split()
    if command[0] == "Change":
        text = text.replace(command[1],command[2])
        print(text)
    elif command[0] == "Includes":
        if command[1] in text:
            print('True')
        else:
            print('False')
    elif command[0] == "End":
        if command[1] == text[len(text)-len(command[1]):]:
            print('True')
        else:
            print('False')
    elif command[0] == "Uppercase":
        text = ''.join([x.upper() for x in text])
        print(text)
    elif command[0] =="FindIndex":
        index = text.find(command[1])
        print(index)
    elif command[0] == "Cut":
        text = text[int(command[1]):int(command[1])+int(command[2])].rstrip()
        print(text)
    command = input()