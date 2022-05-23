number = int(input())
dragon_dic = {}
for el in range(number):
    type_dragon, name_dragon, damage, health, armor = input().split()
    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10
    if type_dragon in dragon_dic and name_dragon in [name for names in dragon_dic[type_dragon] for name in names]:
        index = [x for x in range(len(dragon_dic[type_dragon])) if dragon_dic[type_dragon][x][0] == name_dragon]
        dragon_dic[type_dragon].pop(index[0])
    dragon_dic.setdefault(type_dragon, [])
    dragon_dic[type_dragon].append([name_dragon, int(damage), int(health), int(armor)])
else:
    dragon_dic = {keys: sorted(values) for keys, values in dragon_dic.items()}
    for types, values_data in dragon_dic.items():
        damage_avg = sum([(values_data[x][1]) for x in range(len(values_data))]) / len(values_data)
        health_avg = sum([(values_data[x][2]) for x in range(len(values_data))]) / len(values_data)
        armor_avg = sum([(values_data[x][3]) for x in range(len(values_data))]) / len(values_data)
        print(f'{types}::({damage_avg:.2f}/{health_avg:.2f}/{armor_avg:.2f})')
        [print(
            f"-{values_data[x][0]} -> damage: {values_data[x][1]}, health: {values_data[x][2]}, armor: {values_data[x][3]}")
         for x in range(len(values_data))]
