secret_message = input()
command = input()

while not command == "Reveal":
    command = command.split(":|:")
    if command[0] == 'InsertSpace':
        secret_message = secret_message[:int(command[1])] +" "+ secret_message[int(command[1]):]
        print(secret_message)
    elif command[0] == "Reverse":
        if command[1] in secret_message:
            index = secret_message.find(command[1])
            secret_message = secret_message[:index]+secret_message[index+len(command[1]):] + command[1][::-1]
            print(secret_message)
        else:
            print("error")
    elif command[0] == 'ChangeAll':
        secret_message = secret_message.replace(command[1],command[2])
        print(secret_message)
    command = input()
else:
    print(f"You have a new text message: {secret_message}")