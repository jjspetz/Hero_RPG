import random
import time
from store import *

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if self.alive():
            print("{} attacks {}".format(self.name, enemy.name))
            enemy.receive_damage(self, self.power)
            time.sleep(1.5)

    def receive_damage(self, hero, points):
        if random.randint(1,11) >= self.evade:
            if points > self.armor:
                self.health -= (points - self.armor)
                print("{} received {} damage.".format(self.name, (points-self.armor)))
            else:
                print("Your armor fully protects you!")
            if self.health <= 0:
                print("{} is dead.".format(self.name))
        else:
            print("You evaded the enemy's srtike!")

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Enemy(Character):
    def receive_damage(self, hero, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0 or not self.alive():
            hero.coins += self.bounty
            if self.bounty > 0:
                print("{} is dead. {} receives {} coins as bounty.".format(self.name, hero.name, self.bounty))
            else:
                print("{} is dead.".format(self.name))

class Hero(Character):
    def __init__(self, health=10, power=5, coins=20):
        self.name = 'hero'
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = 0
        self.evade = 0
        self.items = {}

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            item.apply(self)
        else:
            print("You don't have enough.")

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        if random.randint(0,100) < 20:
            enemy.receive_damage(self, 2*self.power)
        else:
            enemy.receive_damage(self, self.power)
        time.sleep(1.5)

    def useitem(self, enemy):
        print(self.items.keys())
        picker = input("What item do you want to use? ")
        if picker in self.items:
            return self.items[picker](enemy)
        else:
            print("You don't own that item...")

class Medic(Hero):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0
        self.items = {}

    def recuperate(self):
        if random.randint(0,100) < 20:
            print("{} recuperate 2 health.".format(self.name))
            self.health += 2

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self, self.power)
        self.recuperate()
        time.sleep(1.5)

class Shadow(Hero):
    def __init__(self, name = "shadow", health = 1, power = 5, coins = 20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = 0
        self.evade = 9
        self.items = {}

class Merchant(Hero):
    def __init__(self):
        self.name = 'merchant'
        self.health = 5
        self.power = 3
        self.coins = 125
        self.armor = 1
        self.evade = 0
        self.items = {}

class Tank(Hero):
    def __init__(self):
        self.name = 'tank'
        self.health = 20
        self.power = 1
        self.coins = 5
        self.armor = 1
        self.evade = 1
        self.items = {}

class Goblin(Enemy):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 2

class Wizard(Enemy):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Zombie(Enemy):
    def __init__(self):
        self.name = "zombie"
        self.health = -500
        self.power = 1
        self.bounty = 0
        self.head = True

    def alive(self):
        return self.head

    def print_status(self):
        print("{} has {} power and is already dead... but still fighting?".format(self.name, self.power))
