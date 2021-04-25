from classes.game import bcolors, Person, Enemy, DevilFruit
from classes.game import DevilFruits as Df


gomu = DevilFruit('gomu', 30, 'paramecia')

Luffy = Person(500, 1000, 50, 40, 50, fruit=Df.gomu)
Zoro = Enemy(600, 600, 35, 45, 35, fruit=None)


choice = Luffy.choose_attack()
dmg = Luffy.generate_damage(choice)

print(f'Oh no! Zoro took {dmg/Zoro.df} damage, his HP is now: ')
print(Zoro.take_damage(dmg))

dmg1 = Zoro.attack()
print(dmg1)

print(f'Oh no! Luffy took {dmg1/Luffy.df} damage, his HP is now: ')
print(Luffy.take_damage(dmg))