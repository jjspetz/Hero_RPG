class Tonic():
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class SuperTonic():
    cost = 5
    name = 'super tonic'
    def apply(self, character):
        character.health += 10
        print("{}'s health increased to {}.".format(character.name, character.health))

class Shortsword():
    cost = 25
    name = 'shortsword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Longsword():
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

class Evade():
    cost = 50
    name = 'cloak of invisibility'
    def apply(self, hero):
        hero.evade += 1
        print("{}'s evade increased by 1 to {}".format(hero.name, hero.evade))

class ZombieKiller():
    cost = 50
    name = 'zombie decapitator'
    def apply(self, hero):
        hero.items[self.name] = self.use
    def use(self, enemy):
        if enemy == "zombie":
            enemy.alive(False)
        else:
            print("You can only use this item on zombies, stupid.")

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Evade, Armor, Tonic, SuperTonic, Shortsword, Longsword, ZombieKiller]
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
