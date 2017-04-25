#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights evil monsters. He has the options to:
1. fight
2. do nothing - in which case the hero will be attacked anyway
3. flee
"""
class Character():
    def __init__(self, health=10, power=5):
        self.health = heath
        self.power = power
    def attack(self,victim):
        victim.health -= self.power
        print("{} does {} damage to the {}.".format(self.name.capitalize(), self.power, victim.name))
        if not victim.alive():
            print("{} is dead.".format(victim.name.capitalize()))
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

class Zombie(Character):
    def __init__(self, health = -500, power = 1, name="zombie"):
        self.name = name
        super().__init__(health, power)
    def alive(self):
        return True
    def print_status(self):
        print("The {} has {} power and is already dead... but still fighting?".format(self.name, self.power))

class Hero(Character):
    def __init__(self, health, power, name="hero"):
        self.name = name
        super().__init__(health, power)
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    def __init__(self, health, power, name="goblin"):
        self.name = name
        super().__init__(health=6, power=2)
    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

def main():
    hero = Hero(10, 5, "JJ")
    goblin = Goblin(6, 2)
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
