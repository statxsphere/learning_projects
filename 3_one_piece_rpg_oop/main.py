from classes.game import bcolors, Person, DevilFruit

gomu = DevilFruit('gomu',30,'paramecia')


Luffy = Person(500, 1000, 50, 40, 50, fruit=gomu)
Zoro = Person(600,600, 35, 45, 35, weapon='great')

print(Zoro.get_maxhp())

choice = Luffy.choose_attack()
dmg = Luffy.generate_damage(choice)

print(f'Oh no! Zoro took {dmg} damage, his HP is now: ')
print(Zoro.take_damage(dmg))
