#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self,victim):
        victim.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, victim.name))
        if not victim.alive():
            print("The {} is dead.".format(victim.name))
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

class Zombie(Character):
    def alive(self):
        return True
    def print_status(self):
        print("The {} has {} power and is already dead... but still fighting?".format(self.name, self.power))

class Hero(Character):
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

def main():
    hero = Hero("JJ", 10, 5)
    goblin = Goblin("goblin", 6, 2)
    zombie = Zombie("zombie", 1, 1)

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
            # Hero attacks goblin
            hero.attack(goblin)
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)

if __name__ == "__main__":
  main()
