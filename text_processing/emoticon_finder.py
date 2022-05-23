seq = input()


for el in range(len(seq)):
    if seq[el] == ":":
        print(seq[el:el+2])