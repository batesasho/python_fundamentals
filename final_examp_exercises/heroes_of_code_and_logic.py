number = int(input())

heroes_dict = {}

for i in range(number):
    heroes = input().split()
    heroes_dict.setdefault(heroes[0],[0,0])
    if  heroes_dict[heroes[0]][0] + int(heroes[1])<=100:
        heroes_dict[heroes[0]][0] += int(heroes[1])
    else:
        heroes_dict[heroes[0]][0] = 100
    if heroes_dict[heroes[0]][1] + int(heroes[2]) <= 200:
        heroes_dict[heroes[0]][1] += int(heroes[2])
    else:
        heroes_dict[heroes[0]][1] = 200
else:
    command = input()
    while not command == "End":
        command = command.split(" - ")
        if command[0] == "CastSpell":
            hero_name,mp_needed,spell_name = command[1],int(command[2]),(command[3])
            if heroes_dict[hero_name][1] >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")

            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        elif command[0] == "TakeDamage":
            hero_name,damage,attacker = command[1],int(command[2]),(command[3])
            if heroes_dict[hero_name][0] > damage:
                heroes_dict[hero_name][0] -= damage
                print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!')

            else:

                print(f"{hero_name} has been killed by {attacker}!")
                heroes_dict.pop(hero_name)
        elif command[0] == "Recharge":
            hero_name,amount = command[1],int(command[2])
            if heroes_dict[hero_name][1] + amount <= 200:

                print(f"{hero_name} recharged for {amount} MP!")
                heroes_dict[hero_name][1] += amount
            else:

                print(f"{hero_name} recharged for {200-heroes_dict[hero_name][1]} MP!")
                heroes_dict[hero_name][1] = 200
        elif command[0] == "Heal":
            hero_name,amount = command[1],int(command[2])
            if heroes_dict[hero_name][0] + amount <= 100:

                print(f"{hero_name} healed for {amount} HP!")
                heroes_dict[hero_name][0] += amount
            else:

                print(f"{hero_name} healed for {100-heroes_dict[hero_name][0]} HP!")
                heroes_dict[hero_name][0] = 100
        command = input()
    else:
        for key,value in sorted(heroes_dict.items(),key = lambda x: (-x[1][0],x[0])):
            print(f'{key}\n  HP: {value[0]}\n  MP: {value[1]}')

