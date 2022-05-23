def calc(num_one,numb_two,operator):
    if operator == "multiply":
        return num_one*numb_two
    elif operator == "divide":
        return int(num_one/numb_two)
    elif operator == "add":
        return num_one+numb_two
    elif operator == "subtract":
        return num_one-numb_two


operator = input()
num_one = int(input())
num_two = int(input())

print(calc(num_one,num_two,operator))