command = input()

while not command == "end":
    print(f"{command} = {command[::-1]}")
    command = input()
