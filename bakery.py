

seq = input().split()

food = {}




for el in range(0,len(seq)):
    if el % 2 == 0:
        food[seq[el]] = int(seq[el+1])
print(food)
