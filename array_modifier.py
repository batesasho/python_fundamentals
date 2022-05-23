array = [i for i in input().split()]
command = input()
is_empty = False
count = 0
while not command == "end":
    count += 1
    action = [int(x) for x in command.split()]
    if action[0] not in range(len(array)) or action[1] not in range(len(array)) or action[0] == action[1]:
        print("Invalid input! Adding additional elements to the board")
        mid_array = int(len(array)/2)
        moves_till_now = int(len(array)/4)
        array [mid_array:mid_array] = [f"-{count}a" for x in range(2)]

    else:
        if array[action[0]] == array[action[1]]:
            print(f"Congrats! You have found matching elements - {array[action[0]]}!")
            array = list(filter((lambda x:  not x == array[action[0]] and not x == array[action[1]]),array))

            if len(array) == 0:
                is_empty = True
                break
        else:
            print("Try again!")

    command = input()
else:
    if len(array) > 0:
        print("Sorry you lose :(")
        print(*array, sep = " ")
if is_empty:
        print(f"You have won in {count} turns!")

