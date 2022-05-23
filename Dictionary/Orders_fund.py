command = input()
products_dict = {}

while not command == "buy":
    command = command.split()
    products_dict.setdefault(command[0],[0,0])
    products_dict[command[0]][0] = float(command[1])
    products_dict[command[0]][1] += int(command[2])
    command = input()
else:
    [print(f"{product} -> {price[0]*price[1]:.2f}") for product,price in products_dict.items()]
