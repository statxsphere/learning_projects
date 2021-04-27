from classes.game import bcolors, Person, Enemy, DevilFruit
from classes.game import DevilFruits as Df


gomu = DevilFruit('gomu', 30, 'paramecia')

Luffy = Person('Luffy', 500, 1000, 50, 40, 50, fruit=Df.gomu)
Zoro = Person('Zoro', 600, 600, 35, 45, 35, fruit=None)

l1 = [Luffy, Zoro]
a=1
for i in l1:
    print(f"{a}. {i.name}")
    a+=1

print(l1[1].name)

ch1 = l1[int(input('Choose your character: ')) - 1]
print(f'You have chosen {ch1.name}.')
ch2 = l1[int(input('Choose enemy: ')) - 1]
print(f'You will be fighting against {ch2.name}.')

enemy = Enemy(ch2.name, ch2.hp, ch2.haki, ch2.haki_attack, ch2.atk, ch2.df, fruit=ch2.fruit, weapon=ch2.weapon)


choice = ch1.choose_attack()
dmg = ch1.generate_damage(choice)

print(f'You attack! {enemy} took {dmg/enemy.df} damage, his HP is now: ')
print(enemy.take_damage(dmg))

dmg1 = enemy.attack()

print(f'Oh no! {ch1} took {dmg1/ch1.df} damage, his HP is now: ')
print(ch1.take_damage(dmg))
