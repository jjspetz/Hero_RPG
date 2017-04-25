#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights evil monsters. He has the options to:
1. fight
2. do nothing - in which case the hero will be attacked anyway
3. flee
"""

from random import randint, random

class Character():
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        if name[0].isupper():
            self.name = name
        else:
            self.name = name.capitalize()
    def attack(self,victim):
        damage = self.power*random()
        victim.health -= damage
        print("{} does {} damage to the {}.".format(self.name, "{0:.2f}".format(damage), victim.name))
        if not victim.alive():
            print("{} is dead.".format(victim.name.capitalize()))
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Zombie(Character):
    def __init__(self, health = -500, power = 1, name="zombie"):
        super().__init__(health, power, name)
    def alive(self):
        return True
    def print_status(self):
        print("The {} has {} power and is already dead... but still fighting?".format(self.name, self.power))

class Hero(Character):
    def __init__(self, health=randint(5,20), power=randint(2,10), name="hero"):
        super().__init__(health, power, name)
    def print_status(self):
        print("You have {} health and {} power.".format("{0:.2f}".format(self.health), self.power))

class Goblin(Character):
    def __init__(self, health=randint(4,8), power=randint(1,5), name="goblin"):
        super().__init__(health, power, name)
    def print_status(self):
        print("The goblin has {} health and {} power.".format("{0:.2f}".format(self.health), self.power))

def enemypicker():
    enemydict = {
                0: Zombie,
                1: Goblin
                }
    
    enemypick = int(input("You have come across a fork in the road. One way leads to a zombie(0), the other leads to a goblin(1). Pick where to go (0-1): "))
    return enemydict[enemypick]()
    

def main():
    hero = Hero(name = "JJ")
    enemy = enemypicker()

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            priority = randint(0,1)
            if priority == 0:
                enemy.attack(hero)
                if hero.alive():
                    hero.attack(enemy)
            else:
                hero.attack(enemy)
                if enemy.alive():
                    enemy.attack(hero)
        elif inpt == "2":
            if enemy.alive():
            # Goblin attacks hero
                enemy.attack(hero)
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))
    
if __name__ == "__main__":
  main()
