import re
num = int(input())
command = input()

list_children = []
while not command == "end":
    key = ''
    for el in command:
        key += chr(ord(el)-num)
    list_children.append(key)

    command= input()
else:
    new_list = []
    pattern = r'(?<=@)([A-Za-z]+)(?:.+?)(?<=!)(G)(?=!)'
    for i in list_children:
        check = re.findall(pattern,i)
        if check:
            new_list.append(check[0][0])
    [print(*new_list,sep="\n")]
