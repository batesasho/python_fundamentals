days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())


money = 0

for day in range(1,days+1):
    money += daily_plunder
    if day %3 ==0:
        money += daily_plunder/2
    if day % 5 == 0:
        money *= 0.7

if money >= expected_plunder:
    print(f"Ahoy! {money:.2f} plunder gained.")
else:
    diff = 100*(money)/expected_plunder
    print(f"Collected only {diff:.2f}% of the plunder.")

