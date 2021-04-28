from classes.game import bcolors, Person, Enemy, DevilFruit, Weapon
from classes.game import DevilFruits as Df
from classes.game import Weapons as Wp


Luffy = Person('Luffy', 500, 1000, 50, 40, 50, fruit=Df.gomu)
Zoro = Person('Zoro', 600, 600, 35, 45, 35, weapon=Wp.Enma)

l1 = [Luffy, Zoro]
a=1
for i in l1:
    print(f"{a}. {i.name}")
    a += 1


ch1 = l1[int(input('Choose your character: ')) - 1]
print(f'You have chosen {ch1.name}.\n')
ch2 = l1[int(input('Choose enemy: ')) - 1]
print(f'You will be fighting against {ch2.name}.\n')

enemy = Enemy(ch2.name, ch2.hp, ch2.haki, ch2.haki_attack, ch2.atk, ch2.df, fruit=ch2.fruit, weapon=ch2.weapon)
running = True

while running:
    choice = ch1.choose_attack()
    dmg = ch1.generate_damage(choice)

    print(f'You attack! {enemy.name} took {dmg/enemy.df} damage, his HP is now: ')
    print(enemy.take_damage(dmg))
    print('')

    if ch1.hp == 0:
        print('Oh no, you lose!')
        break

    if enemy.hp == 0:
        print('Yay! You win.')
        break

    dmg1 = enemy.attack()

    print(f'Oh no! {ch1.name} took {dmg1/ch1.df} damage, his HP is now: ')
    print(ch1.take_damage(dmg))
    print('')

    if ch1.hp == 0:
        print('Oh no, you lose!')
        break

    if enemy.hp == 0:
        print('Yay! You win.')
        break