seq = list(map(int,input().split()))
command = list(map(int,input().split()))

special_num = command[0]
detonation_num = command[1]

while special_num in seq:
    el = seq.index(special_num)
    seq = [ seq[x] for x in range(len(seq)) if x not in range(el - detonation_num, el + detonation_num + 1 )]
print(sum(seq))
