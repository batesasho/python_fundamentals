number = int(input())
list_numbers = []
even = []
odd = []
negative = []
positive = []

for num in range(number):
    list_numbers.append(int(input()))
    if int(list_numbers[num])  % 2 ==0:
        even.append(list_numbers[num])
    else:
        odd.append(list_numbers[num])
    if int(list_numbers[num]) >= 0:
        positive.append(list_numbers[num])
    else:
        negative.append(list_numbers[num])

command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
else:
    print(positive)
