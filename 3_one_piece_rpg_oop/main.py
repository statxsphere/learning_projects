from classes.game import bcolors, Person, DevilFruit
from classes.game import DevilFruits as Df


gomu = DevilFruit('gomu', 30, 'paramecia')


Luffy = Person(500, 1000, 50, 40, 50, fruit=Df.gomu)
Zoro = Person(600,600, 35, 45, 35, fruit=None)

print(Luffy.get_fruit_dmg())
print(Zoro.get_maxhp())

choice = Luffy.choose_attack()
dmg = Luffy.generate_damage(choice)

print(f'Oh no! Zoro took {dmg/Zoro.df} damage, his HP is now: ')
print(Zoro.take_damage(dmg))
