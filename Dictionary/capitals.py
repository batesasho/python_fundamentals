country = input().split(", ")
capital = input().split(", ")

dictionary = {}

dictionary = {print(f"{key} -> {value}") for key,value in zip(country,capital)}

