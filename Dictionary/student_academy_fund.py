number = int(input())
stats_dict = {}
for el in range(1,number+1):
    name = input()
    grade = float(input())
    stats_dict.setdefault(name,[])
    stats_dict[name].append(grade)
else:
    [print(f"{name} -> {sum(grade)/len(grade):.2f}") for name,grade in sorted(stats_dict.items(),key = lambda x: -sum(x[1])/len(x[1])) if sum(grade)/len(grade) >= 4.5]
