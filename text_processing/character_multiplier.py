from itertools import zip_longest

command = input()
str_one = command.split()[0]
str_two = command.split()[1]
new = 0
current_sum = 0

for el_one,el_two in zip_longest(str_one,str_two,fillvalue=chr(1)):
    current_sum = ord(el_one) * ord(el_two)
    new += current_sum
print(new)





