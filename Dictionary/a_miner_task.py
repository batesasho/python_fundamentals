command = input()
dictionary = {}
while not command == "stop":
    resource = command
    quantity = int(input())
    dictionary.setdefault(resource,0)
    dictionary[resource] += quantity
    command = input()
else:
    for res,quan in dictionary.items():
        print(f"{res} -> {quan}")
