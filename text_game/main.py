# text based game

import random
import time

class Player():
    def normal_atk(self):
        attack = random.randint(0, 15)
        return attack

    def spec_attack(self):
        spec_atk = random.randint(20, 40)
        return spec_atk

    def heal(self):
        healing = random.randint(5, 25)
        return healing

def first_go():
    go = random.randint(0, 2)
    if go == 0:
        return 'Comp'
    else:
        return name

player_hp = 100
player_energy = 0

comp_hp = 100
comp_energy = 0

ready = input("are you ready to play? Type Y/N: ")
name = input("Please enter your name: ")
turn = first_go()

player = Player()
comp = Player()

while player_hp > 0 and comp_hp > 0:
    print(f"\n{turn}'s turn")
    if turn != 'Comp':
        action = int(input(f"{name}, please choose an action:\n1) Normal Attack\n2) Special Attack\n3) Heal\n"))
        if action == 1:
            player_normal_attack = player.normal_atk()
            comp_hp = comp_hp - player_normal_attack
            player_energy += 10
            time.sleep(1)
            print(f"\n{name} just did {player_normal_attack} damage!")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(1)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = 'Comp'
        elif action == 2 and player_energy >= 20:
            player_special_attack = player.spec_attack()
            comp_hp = comp_hp - player_special_attack
            player_energy -= 20
            time.sleep(1)
            print(f"\n{name} just did {player_special_attack} damage!")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(1)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = 'Comp'
        elif action == 3 and player_energy >= 15:
            player_heal = player.heal()
            player_hp += player_heal
            player_energy -= 15
            time.sleep(1)
            print(f"\n{name} just healed themselves for {player_heal}")
            print(f"{name} has {player_hp} health and {player_energy} energy")
            turn = 'Comp'
        elif action == 2 or action == 3 and player_energy < 15:
            print(f"\n{name} you have {player_hp} health and {player_energy} energy")
            print(f"\n{name} your energy is too low, please choose 1) Normal Attack: ")
        else:
            print("Please enter a correct action")
    else:
        if comp_energy >= 20:
            comp_spec_attack = comp.spec_attack()
            player_hp = player_hp - comp_spec_attack
            comp_energy -= 20
            time.sleep(1)
            print(f"\nThe computer just did {comp_spec_attack} damage")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(1)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = name
        elif comp_hp < 50 and comp_energy >= 15:
            comp_healing = comp.heal()
            comp_hp += comp_healing
            comp_energy -= 15
            time.sleep(1)
            print(f"\nThe comp has healed themselves for {comp_healing}")
            print(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(1)
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = name
        else:
            comp_norm_attack = comp.normal_atk()
            player_hp = player_hp - comp_norm_attack
            comp_energy += 10
            time.sleep(1)
            print(f"\nComp just did {comp_norm_attack} damage!")
            print(f"\n{name} now has {player_hp} health and {player_energy} energy")
            print(f"The computer now has {comp_hp} health and {comp_energy} energy")
            turn = name

if player_hp <= 0:
    print("The computer has won this round!")
elif comp_hp <= 0:
    print(f"\n{name} has won this round!")


