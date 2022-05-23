number = input().split()
half_list = (len(number)//2)
number = [int(x) for x in number]
left_racer = number[:half_list]
right_racer = number[-1:-half_list-1:-1]

final_time_left = 0
final_time_right = 0

for time in range(len(left_racer)):
    final_time_left += left_racer[time]
    final_time_right += right_racer[time]
    if left_racer[time] == 0:
        final_time_left *= 0.8
    if right_racer[time] == 0:
        final_time_right *= 0.8

if final_time_right > final_time_left:
    print(f"The winner is left with total time: {final_time_left:.1f}")
elif final_time_right < final_time_left:
    print(f"The winner is right with total time: {final_time_right:.1f}")

