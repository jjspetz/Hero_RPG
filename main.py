#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""

class Hero():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self,victim):
        victim.health -= self.power
            print("You do {} damage to the goblin.".format(self.power))
            if victim.health <= 0:
                print("The goblin is dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, victim):
        victim.health -= self.power
            print("The goblin does {} damage to you.".format(self.power))
            if victim.health <= 0:
                print("You are dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

def main():
    JJ = Hero(10, 5)
    goblin = Goblin(6, 2)

    while goblin.alive() and JJ.alive():
        JJ.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            # Hero attacks goblin
            JJ.attack(goblin)
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(JJ)

if __name__ == "__main__":
  main()
