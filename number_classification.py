numbers_string = input().split(", ")
numbers_string = list(map(int, numbers_string))
print("Positive: ",end=""),print(*[x for x in numbers_string if x >= 0],sep=", ")
print("Negative: ",end = ""),print(*[x for x in numbers_string if x <0],sep=", ")
print("Even: ",end=""),print(*[x for x in numbers_string if x % 2 == 0],sep=", ")
print("Odd: ",end = ""),print(*[x for x in numbers_string if not x % 2 ==0],sep=", ")