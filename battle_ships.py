number = int(input())
ships_list = []
destroyed_ships = 0
for num in range(1,number+1):
    command = input().split()
    ships_list.append([int(x) for x in command])

squares_attack = input().split()
for el in range(len(squares_attack)):
    ship_position_row = int(squares_attack[el][0])
    ship_position_col = int(squares_attack[el][-1])
    if ships_list[ship_position_row][ship_position_col] - 1 > 0:
        ships_list[ship_position_row][ship_position_col] -= 1
    elif ships_list[ship_position_row][ship_position_col] -1  == 0:
        ships_list[ship_position_row][ship_position_col] -= 1
        destroyed_ships += 1
else:
    print(destroyed_ships)


