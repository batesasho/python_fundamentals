
seq = input().split("|")
new_list = []
for el in range(len(seq)-1,-1,-1):
    new = seq[el].split()
    new_list.extend(new)


print(*new_list)