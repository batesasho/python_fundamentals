number = int(input())
parking_dic = {}
for num in range(1,number+1):
    command = input().split()
    if command[0] == "register":
        if command[1] not in parking_dic:
            print(f"{command[1]} registered {command[2]} successfully")
            parking_dic[command[1]] = command[2]
        else:
            print(f"ERROR: already registered with plate number {command[2]}")
    else:
        if command[1] not in parking_dic:
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"{command[1]} unregistered successfully")
            del parking_dic[command[1]]
else:
    [print(f"{name} => {plate}") for name,plate in parking_dic.items()]