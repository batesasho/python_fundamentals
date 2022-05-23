import math

budget = float(input())
number_students = int(input())
price_single_floar = float(input())
price_single_egg = float(input())
price_apron = float(input())



count_floar = 0
count_egg = 0
count_arpon = 0

for i in range(1,number_students+1):
    count_egg += 10
    count_arpon += 1
    if i % 5 == 0:
        count_floar += 0
    else:
        count_floar += 1


price_egg = count_egg * price_single_egg
price_floar = count_floar*price_single_floar
price_arpon = math.ceil(count_arpon*1.2)*price_apron

total_price = price_egg+price_floar+price_arpon

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    diff = abs(total_price-budget)
    print(f"{diff:.2f}$ more needed.")
