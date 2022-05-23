dictionary_el = {}
command = input().split()
while bool(command):
    for el in range(0, len(command), 2):
        dictionary_el.setdefault(command[el + 1], [])
        dictionary_el[command[el + 1]].append(int(command[el]))
        if "Shards".lower() in dictionary_el and sum(dictionary_el[("Shards".lower())]) >= 250:
            print(f"Shadowmourne obtained!")
            dictionary_el["Shards".lower()] -= 250

        elif "Fragments".lower() in dictionary_el and sum(dictionary_el[("Fragments".lower())]) >= 250:
            print(f"Valanyr obtained!")
            dictionary_el["Fragments".lower()] -= 250

        elif "Motes".lower() in dictionary_el and sum(dictionary_el[("Motes".lower())]) >= 250:
            print(f"Dragonwrath obtained!")
            dictionary_el["Motes".lower()] -= 250

    command = input().split()
