def pickhero():
    heroes = [Tank, Medic, Merchant, Hero, Shadow]
    print("Tank(0), Medic(1), Merchant(2), Hero(3), Shadow(4)")
    reply = int(input("Which hero do you want to be? "))
    return heroes[reply]()

hero = pickhero()
