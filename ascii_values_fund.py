seq = input().split(", ")

dictionary = {}

for el in seq:
    dictionary.setdefault(el,ord(el))


print(dictionary)