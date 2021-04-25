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

ch1 = l1[int(input('Choose your character: ')) - 1].name
ch2 = l1[int(input('Choose enemy: ')) - 1].name


for i in l1:
    if i.name == ch2:
        enemy = Enemy(i.name, i.hp, i.haki, i.haki_attack, i.atk, i.df, fruit=i.fruit, weapon=i.weapon)



choice = Luffy.choose_attack()
dmg = Luffy.generate_damage(choice)

print(f'Oh no! Zoro took {dmg/enemy.df} damage, his HP is now: ')
print(enemy.take_damage(dmg))

dmg1 = enemy.attack()

print(f'Oh no! Luffy took {dmg1/Luffy.df} damage, his HP is now: ')
print(Luffy.take_damage(dmg))
