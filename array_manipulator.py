seq = list(map(int, input().split()))

command = input()

while not command == "print":
    command = command.split()

    if command[0] == "add":
        seq.insert(int(command[1]), int(command[2]))
    elif command[0] == "addMany":
        seq[int(command[1]):int(command[1])] = [int(command[x]) for x in range(2, len(command))]
    elif command[0] == "contains":
        if int(command[1]) in seq:
            print(seq.index(int(command[1])))
        else:
            print(-1)
    elif command[0] == "remove":
        seq.pop(int(command[1]))
    elif command[0] == "shift":
        seq = seq[seq.index(int(command[1])) + 1:] + seq[:seq.index(int(command[1])) + 1]
    elif command[0] == "sumPairs":
        seq = [sum(seq[n:n + 2]) for n in range(0, len(seq), 2)]

    command = input()
else:
    print(seq)
