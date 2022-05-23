vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']

print(*[x for x in input() if x not in vowels],sep = "")