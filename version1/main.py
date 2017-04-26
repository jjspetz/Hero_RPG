#!/usr/bin/env python3

"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= (points - self.armor)
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Enemy(Character):
    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            hero.coins += self.bounty
            print("{} is dead. {} receives {} coins as bounty.".format(self.name, hero.name, self.bounty))

class Hero(Character):
    def __init__(self, health=10, power=5, coins=20):
        self.name = 'hero'
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = 0

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        if random.randint(0,100) < 20:
            enemy.receive_damage(2*self.power)
        else:
            enemy.receive_damage(self.power)
        time.sleep(1.5)

class Medic(Hero):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 5
        self.coins = 20

    def recuperate(self):
        if random.randint(0,100) < 20:
            print("{} recuperate 2 health.".format(self.name))
            self.health += 2

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
        self.recuperate()
        time.sleep(1.5)

class Shadow(Hero):
    def __init__(self, name = "shadow", health = 1, power = 5, coins = 20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def receive_damage(self, points):
        if random.randint(0,10) == 0:
            self.health -= points
            print("{} received {} damage.".format(self.name, points))
            if self.health <= 0:
                print("{} is dead.".format(self.name))
        else:
            print("{} dodges enemy attack.".format(self.name))

class Merchant(Hero):
    def __init__(self):
        self.name = 'merchant'
        self.health = 5
        self.power = 3
        self.coins = 125

class Tank(Hero):
    def __init__(self):
        self.name = 'tank'
        self.health = 20
        self.power = 3
        self.coins = 5

    def receive_damage(self, points):
        if random.randint(0,10) < 5:
            print("{} defends against some damage.".format(self.name))
            self.health -= (points-(1+self.armor))
            print("{} received {} damage.".format(self.name, points-1))
            if self.health <= 0:
                print("{} is dead.".format(self.name))
        else:
            self.health -= (points - self.armor)
            print("{} received {} damage.".format(self.name, points))
            if self.health <= 0:
                print("{} is dead.".format(self.name))

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
        self.bounty = 10000

    def alive(self):
        return True
    def print_status(self):
        print("{} has {} power and is already dead... but still fighting?".format(self.name, self.power))


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
            print("3. flee")
            print("> ", end=' ')
            reply = int(input())
            if reply == 1:
                hero.attack(enemy)
            elif reply == 2:
                if hero.name == "medic":
                    hero.recuperate()
                pass
            elif reply == 3:
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

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class SuperTonic(object):
    cost = 5
    name = 'super tonic'
    def apply(self, character):
        character.health += 10
        print("{}'s health increased to {}.".format(character.name, character.health))

class Shortsword(object):
    cost = 25
    name = 'shortsword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Longsword(object):
    cost = 100
    name = 'longsword'
    def apply(self, hero):
        hero.power += 5
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Armor():
    cost = 50
    name = "armor"
    def apply(self, hero):
        hero.armor += 2
        print("{}'s armor increased by 2 to {}".format(hero.name, hero.armor))

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Armor, Tonic, SuperTonic, Shortsword, Longsword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            reply = int(input("> "))
            if reply == 10:
                break
            else:
                ItemToBuy = Store.items[reply - 1]
                item = ItemToBuy()
                hero.buy(item)

if __name__ == "__main__":
    hero = Tank()
    enemies = [Zombie(), Goblin(), Wizard()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.do_shopping(hero)

    print("YOU WIN!")
