single_string =(input()).split(", ")
number_beggars = int(input())

i=0
sum_beggars = []
for num in range(1,number_beggars+1):
        beggars_incomes = []
        for index in range(i,len(single_string),number_beggars):
            beggars_incomes.append(int(single_string[index]))

        sum_beggars.append(sum(beggars_incomes))
        i += 1
else:
    print(sum_beggars)



