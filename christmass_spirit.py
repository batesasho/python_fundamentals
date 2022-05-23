decoration_qunatity = int(input())
days_till_christmass = int(input())
price = 0
spirit = 0

for day in range(1,days_till_christmass+1):
    if day% 11 == 0:
        decoration_qunatity += 2
    if day %2 == 0:
        price += 2 * decoration_qunatity
        spirit += 5
    if day %3 ==0:
        price +=8*decoration_qunatity
        spirit += 13
    if day %5 ==0:
        price +=15*decoration_qunatity
        spirit += 17
        if day % 3 == 0:
            spirit +=30
    if day %10 ==0:
        spirit -=20
        price += 23
if days_till_christmass %10 == 0:
        spirit -= 30

print(f"Total cost: {price}")
print(f"Total spirit: {spirit}")