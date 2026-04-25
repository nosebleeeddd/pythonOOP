import os
from character import Hero, Enemy
from weapons import glock_pistol, pocket_knife, fists

hero = Hero(name="Hero", health=100)
hero.equip(pocket_knife)
enemy = Enemy(name="Enemy", health=100, weapon=fists)

while True:
    # clear screen on windows and linux
    os.system('cls' if os.name == 'nt' else 'clear')

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()

