#!/usr/bin/env python3

"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import time
from characters import *
from store import *


class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the {}".format(enemy.name))
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. use item")
            print("4. flee")
            print("> ", end=' ')
            reply = int(input())
            if reply == 1:
                hero.attack(enemy)
            elif reply == 2:
                if hero.name == "medic":
                    hero.recuperate()
                pass
            elif reply == 3:
                hero.useitem(enemy)
            elif reply == 4:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid reply {}".format(input))
                continue
            enemy.attack(hero)
        if hero.alive():
            print("You defeated the {}".format(enemy.name))
            return True
        else:
            print("YOU LOSE!")
            return False


def pickhero():
    heroes = [Tank, Medic, Merchant, Hero, Shadow]
    print("Tank(0), Medic(1), Merchant(2), Hero(3), Shadow(4)")
    reply = int(input("Which hero do you want to be? "))
    return heroes[reply]()

if __name__ == "__main__":
    hero = pickhero()

    enemies = [Goblin(), Wizard(), Zombie()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.do_shopping(hero)

    print("YOU WIN!")
