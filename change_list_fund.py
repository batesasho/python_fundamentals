seq = list(map(int,input().split()))
command = input().split()

while not command[0] == "Odd" and not command[0] == "Even":

    if command[0] == "Delete":
        seq = list(filter(lambda x: not x == int(command[1]),seq))
    elif command[0] == "Insert":
        seq.insert(int(command[2]),int(command[1]))
    command = input().split()
else:
    if command[0] == "Odd":
        print(*[x for x in seq if not x %2 == 0 ], sep = " ")
    else:
        print(*[x for x in seq if  x % 2 == 0], sep=" ")


