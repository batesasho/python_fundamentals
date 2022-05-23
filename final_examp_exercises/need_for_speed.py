number = int(input())

car_dict = {}

for i in range(number):
    car_info = input().split("|")
    car_dict.setdefault(car_info[0],[int(car_info[1]),int(car_info[2])])

else:
    command = input()

    while not command == "Stop":
        command = command.split(" : ")
        if command[0] == "Drive":
            if car_dict[command[1]][1] >= int(command[3]):
                car_dict[command[1]][0] += int(command[2])
                car_dict[command[1]][1] -= int(command[3])
                print(f"{command[1]} driven for {command[2]} kilometers. {command[3]} liters of fuel consumed.")
                if car_dict[command[1]][0] >= 100000:
                    print(f"Time to sell the {command[1]}!")
                    car_dict.pop(command[1])
            else:
                print("Not enough fuel to make that ride")
        elif command[0] == "Refuel":
            current_tank = int(car_dict[command[1]][1])
            if car_dict[command[1]][1] + int(command[2]) <= 75:
                car_dict[command[1]][1] += int(command[2])
                print(f'{command[1]} refueled with {int(command[2])} liters')
            else:
                car_dict[command[1]][1] = 75
                print(f'{command[1]} refueled with {75 - current_tank} liters')

        elif command[0] == "Revert":
            car_dict[command[1]][0] -= int(command[2])
            if car_dict[command[1]][0] < 10000:
                car_dict[command[1]][0] = 10000
            else:
                print(f"{command[1]} mileage decreased by {command[2]} kilometers")
        command = input()
    else:
        [print(f"{car} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.") for car,value in sorted(car_dict.items(),key=lambda x:(-x[1][0],x[0]))]