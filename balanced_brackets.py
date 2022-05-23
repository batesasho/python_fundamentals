number = int(input())
string = []
count_open_brackets = 0
count_closed_brackets = 0
not_balanced = False
is_consecutive = 0
for num in range(1, number + 1):
    string.append(input())
    if string[num - 1] == "(":
        count_open_brackets += 1
        is_consecutive += 1
        if is_consecutive == 2:
            not_balanced == True
            break
    elif string[num - 1] == ")":
        is_consecutive -= 1
        count_closed_brackets += 1
if not (count_open_brackets == count_closed_brackets) or not_balanced == True:
    print("UNBALANCED")
else:
    print("BALANCED")
