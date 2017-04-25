#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights evil monsters. He has the options to:
1. fight
2. do nothing - in which case the hero will be attacked anyway
3. flee
"""

from random import randint, random

YES = ('y', 'Y', 'yes', 'YES', 'Yes', 'OK', 'Okay', 'yeah', 'Yeah')

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
            print("{} is dead.".format(victim.name))
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Hero(Character):
    def __init__(self, initiative=random(), health=randint(5,20), power=randint(2,10), name="hero"):
        self.initiative = initiative
        self.maxhealth = health
        super().__init__(health, power, name)
    def print_status(self):
        print("You have {} health, {} power, and an initiative of {}."
        .format("{0:.2f}".format(self.health), self.power, int(self.initiative * 100)))
    def rest(self):
        if self.health < self.maxhealth - 2:
            self.health = self.health + 2
        else:
            self.health = self.maxhealth
        print("Your health is {}".format(self.health))

class Goblin(Character):
    def __init__(self, health=randint(4,8), power=randint(1,5), name="goblin"):
        super().__init__(health, power, name)
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, "{0:.2f}".format(self.health), self.power))

class Orc(Character):
    def __init__(self, health=randint(15,30), power=randint(3,8), name="orc"):
        super().__init__(health, power, name)
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, "{0:.2f}".format(self.health), self.power))

class Zombie(Character):
    def __init__(self, health = -500, power = 1, name="zombie"):
        super().__init__(health, power, name)
    def alive(self):
        return True
    def print_status(self):
        print("{} has {} power and is already dead... but still fighting?".format(self.name, self.power))

class Skeleton(Character):
    def __init__(self, health = -100, power = randint(1,4), name="skeleton"):
        super().__init__(health, power, name)
    def alive(self):
        return True
    def print_status(self):
        print("{} has {} power and is already dead... but still fighting?".format(self.name, self.power))

def enemypicker():
    enemydict = {
                1: Zombie,
                2: Goblin,
                3: Skeleton,
                4: Orc
                }

    enemypick = int(input("The scouting report indicates danger lies ahead...\n \
    Option 1: Charge the zombie. Option 2: Hurl yourself at the goblin.\n \
    Option 3: Moonwalk to the skeleton. Option 4: Sneak up on the Orc.\n \
    Pick where to go (1-4): "))

    return enemydict[enemypick]()

def attacksequence():
    enemy = enemypicker()
    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. drink a potion")
        print("4. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            priority = random()+ hero.initiative
            if priority < 0.8:
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
            hero.rest()
            enemy.attack(hero)
            pass    
        elif inpt == "4":
            print("You run like a coward.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

def main():
    while True:
        attacksequence()
        if not hero.alive():
            print("RIP")
            break
        else:
            switch = input("Do you want to rest? (y or n) ")
            if switch in YES:
                hero.rest()

hero = Hero(name = input("Mighty hero, what's your name? "))

if __name__ == "__main__":
  main()
