from classes.game import Person, Enemy, attack
from classes.game import DevilFruits as Df
from classes.game import Weapons as Wp
from classes.game import FColors as col


Luffy = Person('Luffy', 500, 1000, 50, 40, 50, fruit=Df.gomu)
Zoro = Person('Zoro', 600, 600, 35, 45, 35, weapon=[Wp.enma, Wp.s_kitetsu, Wp.w_ichimonji])

l1 = [Luffy, Zoro]
a=1
for i in l1:
    print(f"{a}. {i.get_name()}")
    a += 1


ch1 = l1[int(input('Choose your character: ')) - 1]
print(f'You have chosen {ch1.get_name()}.\n')
ch2 = l1[int(input('Choose enemy: ')) - 1]
print(f'You will be fighting against {ch2.get_name()}.\n')

enemy = Enemy(ch2.get_name(), ch2.get_hp(), ch2.get_haki(), ch2.get_haki_cost(), ch2.get_atk(), ch2.get_df(),
              fruit=ch2.get_devil_fruit(), weapon=ch2.get_weapon())

running = True
while running:
    choice1 = ch1.choose_action()
    dmg1 = attack(enemy)

    if choice1 == 1:
        choice = ch1.choose_attack()
        dmg = ch1.generate_damage(choice)

        print(f'You attack! {enemy.get_name()} took {dmg / enemy.get_df()} damage, his HP is now: ')
        print(enemy.take_damage(dmg))
        print('')

    if choice1 == 2:
        dmg1 = dmg1 - ch1.get_df()
        if dmg1 < 0:
            dmg1 = 0

    if choice1 == 3:
        dmg1 = ch1.dodge(dmg1)

    if ch1.get_hp() == 0:
        print('Oh no, you lose!')
        break

    if enemy.get_hp() == 0:
        print('Yay! You win.')
        break

    if dmg1 > 0:
        print(f'Oh no! {ch1.get_name()} took {dmg1 / ch1.get_df()} damage, his HP is now: ')
        print(ch1.take_damage(dmg1))
        print('')
    else:
        print(f'{ch1.get_name()} did not take any damage! His current HP is:')
        print(ch1.take_damage(dmg1))
        print('')

    if ch1.get_hp() == 0:
        print('Oh no, you lose!')
        break

    if enemy.get_hp() == 0:
        print('Yay! You win.')
        break
