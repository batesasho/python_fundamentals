seq = input().split("|")

command = input().split()

even = []
odd = []

while not command[0] == "Done":

    if command[0] == "Remove":
        if int(command[1]) in range(len(seq)):
            seq.pop(int(command[1]))
    elif command[0] == "Add":
        if int(command[2]) in range(len(seq)):
            seq.insert(int(command[2]),(command[1]))
    elif command[0] == "Check":
        if command[1] == "Even" :
            for el in range(len(seq)):
                if el % 2 == 0:
                    even.append(seq[el])
            print(*even,sep=" ")
        else:
            for el in range(len(seq)):
                if not el % 2 == 0:
                    odd.append(seq[el])
            print(*odd,sep= " ")
    command = input().split()
else:
    print(f"You crafted {''.join(seq)}!")

