time_leaving = input().split(':')
steps_taken = int(input())
time_seconds_each_step = int(input())

time_total_steps = steps_taken*time_seconds_each_step

hours = time_leaving[0]
minutes = time_leaving[1]
seconds = time_leaving[2]





print(f'Time Arrival: {hours}:{minutes}:{seconds}')