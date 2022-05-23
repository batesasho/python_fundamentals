text = input()

dictionary = {}

for el in text:
    dictionary.setdefault(el,0)
    dictionary[el] +=1

dictionary.pop(" ")
for key,value in dictionary.items():
    print(f"{key} -> {value}")