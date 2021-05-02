from classes.game import Person, Enemy
from classes.game import DevilFruits as Df
from classes.game import Weapons as Wp
from classes.game import FColors as col


Luffy = Person('Luffy', 500, 1000, 50, 40, 50, fruit=Df.gomu)
Zoro = Person('Zoro', 600, 600, 35, 45, 35, weapon=Wp.Enma)

l1 = [Luffy, Zoro]
a=1
for i in l1:
    print(f"{a}. {i.__name}")
    a += 1


ch1 = l1[int(input('Choose your character: ')) - 1]
print(f'You have chosen {ch1.__name}.\n')
ch2 = l1[int(input('Choose enemy: ')) - 1]
print(f'You will be fighting against {ch2.__name}.\n')

enemy = Enemy(ch2.__name, ch2.__hp, ch2.__haki, ch2.__haki_attack, ch2.__atk, ch2.__df, fruit=ch2.__fruit, weapon=ch2.__weapon)
running = True

while running:
    choice1 = ch1.choose_action()
    dmg1 = enemy.attack()

    if choice1 == 1:
        choice = ch1.choose_attack()
        dmg = ch1.generate_damage(choice)

        print(f'You attack! {enemy.__name} took {dmg / enemy.__df} damage, his HP is now: ')
        print(enemy.take_damage(dmg))
        print('')

    if choice1 == 2:
        dmg1 = dmg1 - ch1.__df
        if dmg1 < 0:
            dmg1 = 0

    if choice1 == 3:
        dmg1 = ch1.dodge(dmg1)

    if ch1.__hp == 0:
        print('Oh no, you lose!')
        break

    if enemy.__hp == 0:
        print('Yay! You win.')
        break

    if dmg1 > 0:
        print(f'Oh no! {ch1.__name} took {dmg1 / ch1.__df} damage, his HP is now: ')
        print(ch1.take_damage(dmg1))
        print('')
    else:
        print(f'{ch1.__name} did not take any damage! His current HP is:')
        print(ch1.take_damage(dmg1))
        print('')

    if ch1.__hp == 0:
        print('Oh no, you lose!')
        break

    if enemy.__hp == 0:
        print('Yay! You win.')
        break