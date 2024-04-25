from random import randint

npcs_list = []


def create_monster():
    level = randint(0, 100)

    new_npc = {
        'name': f"Monster #{level}",
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level
    }

    return new_npc


def generate_monsters(n_npcs):
    for x in range(n_npcs):
        new_npc = create_monster()
        npcs_list.append((new_npc))


def show_npcs():
    for npc in npcs_list:
        print(f"Nome: {npc['name']} // Leve: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']}")


generate_monsters(5)
show_npcs()
