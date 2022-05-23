command = input()
new = ''

el=0
while el < len(command):
    if not el+1 == len(command):
        if not command[el] == command[el+1]:
            new += command[el]
    else:
         new += command[-1]
    el += 1
else:
    print(new)


