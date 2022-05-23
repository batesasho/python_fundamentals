num = int(input())
piano_dict = {}
for i in range(num):
    piano_pieces = input().split("|")
    piano_dict.setdefault(piano_pieces[0],[piano_pieces[1],piano_pieces[2]])
else:
    command = input()
    while not command == "Stop":
        command = command.split("|")
        name_pieces = command[1]
        if command[0] == "Add":
            composer,key = command[2],command[3]
            if name_pieces in piano_dict:
                print(f"{name_pieces} is already in the collection!")
            else:
                print(f"{name_pieces} by {composer} in {key} added to the collection!")
                piano_dict[name_pieces] = [composer,key]
        elif command[0] == "Remove":
            
            if name_pieces in piano_dict:
                piano_dict.pop(name_pieces)
                print(f"Successfully removed {name_pieces}!")
            else:
                print(f"Invalid operation! {name_pieces} does not exist in the collection.")
        elif command[0] == "ChangeKey":
            if name_pieces in piano_dict:
                new_key = command[2]
                piano_dict[name_pieces][1] = new_key
                print(f"Changed the key of {name_pieces} to {new_key}!")
            else:
                print(f"Invalid operation! {name_pieces} does not exist in the collection.")
        command=input()
    else:
        [print(f"{name} -> Composer: {value[0]}, Key: {value[1]}") for name,value in sorted(piano_dict.items(),key=lambda x:(x[0],x[1][0]))]