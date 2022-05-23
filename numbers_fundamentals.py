seq_integers = sorted([int(x) for x in input().split()],reverse=True)
average_num = sum(seq_integers)/len(seq_integers)
filtered_list = list(filter(lambda x:x>average_num,seq_integers))

if filtered_list:
    print(*filtered_list[:5])
else:
    print("No")



