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
        print("{} has {} power and is already dead... but still fighting?"
        .format(self.name, self.power))

class Hero(Character):

    def __init__(self, initiative=random(), health=randint(5,20), power=randint(2,10), name="hero"):
        self.initiative = initiative
        super().__init__(health, power, name)

    def print_status(self):
        print("You have {} health, {} power, and an initiative of {}."
        .format("{0:.2f}".format(self.health), self.power, int(self.initiative * 100)))

class Goblin(Character):
    def __init__(self, health=randint(4,8), power=randint(1,5), name="goblin"):
        super().__init__(health, power, name)
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, "{0:.2f}".format(self.health), self.power))

def main():
    hero = Hero(name = "JJ")
    goblin = Goblin(name="Tanweer")
    zombie = Zombie()

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            priority = random()+ hero.initiative
            if priority < 0.8:
                goblin.attack(hero)
                if hero.alive():
                    hero.attack(goblin)
            else:
                hero.attack(goblin)
                if goblin.alive():
                    goblin.attack(hero)
        elif inpt == "2":
            if goblin.alive():
            # Goblin attacks hero
                goblin.attack(hero)
            pass
        elif inpt == "3":
            print("You run like a coward.")
            enemypicker()
        else:
            print("Invalid inpt {}".format(inpt))

if __name__ == "__main__":
  main()
