import random


class FColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# devil_fruits = [{'name':'gomu', 'dmg':40, 'range':'long'},
#                 {'name':'mera', 'dmg':50, 'range':'medium'},
#                 {'name':'gura', 'dmg':80, 'range':'v_long'}]
#
#
# def fruit_finder(x):
#     for i in devil_fruits:
#         if i['name'] == x:
#             return i['dmg']
#
#
# sword = {'good':40,'great':60,'supreme':80}

class DevilFruit:
    def __init__(self, name, damage, type, special=None):
        self.__name = name
        self.__dmg = damage
        self.__type = type
        self.__spl = special

    def get_dmg(self, attack):
        return attack + self.__dmg

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_special(self):
        return self.__spl


class Weapon:
    def __init__(self, name, damage, grade):
        self.__name = name
        self.__dmg = damage
        self.__grade = grade
        self.__use_count = 0

    def weapon_use(self):
        self.__use_count += 1

    def get_dmg(self, attack):
        return attack + self.__dmg


class DevilFruits:
    gomu = DevilFruit('Gomu Gomu No Mi', 30, 'paramecia')


class Weapons:
    Enma = Weapon('Enma', 30, 'Great')


class Person:
    def __init__(self, name, hp, haki, hcost, atk, df, fruit=None, weapon=None):
        self.__name = name
        self.__maxhp = hp
        self.__hp = hp
        self.__maxhaki = haki
        self.__haki = haki
        self.__haki_attack = hcost
        self.__atk = atk
        self.__atkh = atk + 10
        self.__atkl = atk - 10
        self.__df = df
        self.__weapon = weapon
        self.__fruit = fruit
        self.__fruit_attack = self.__fruit.get_dmg(self.__atk) if fruit else None
        self.__actions = ['Attack', 'Block', 'Dodge']
        if not self.__fruit and not self.__weapon:
            self.__attacks = ['Melee', 'Armament Haki']
        elif self.__fruit and not self.__weapon:
            self.__attacks = ['Melee', 'Armament Haki', 'Devil Fruit Attack', 'Armament: Devil Fruit']
        elif self.__weapon and not self.__fruit:
            self.__attacks = ['Melee', 'Armament Haki', 'Use Weapon', 'Armament: Weapon']
        elif self.__weapon and not self.__fruit:
            self.__attacks = ['Melee', 'Armament Haki', 'Devil Fruit Attack', 'Armament: Devil Fruit',
                              'Use Weapon', 'Armament: Weapon']

    def get_fruit_dmg(self):
        return random.randint(self.__fruit_attack - 10, self.__fruit_attack + 10) if self.__fruit else 0

    def take_damage(self, dmg):
        self.__hp -= dmg / self.__df
        if self.__hp < 0:
            self.__hp = 0
        return self.__hp

    def get_hp(self):
        return self.__hp

    def get_maxhp(self):
        return self.__maxhp

    def get_haki(self):
        return self.__haki

    def get_maxhaki(self):
        return self.__maxhaki

    def take_haki(self, haki_used):
        self.__haki -= haki_used

    def get_devil_fruit(self):
        return self.__fruit

    def get_haki_cost(self):
        return self.__haki_attack

    def choose_action(self):
        print('What will you do?\n')
        i = 1
        for item in self.__actions:
            print(str(i)+": "+item)
            i += 1
        print('')
        choice = int(input('Make a choice: '))
        return choice

    def choose_attack(self):
        print('What attack will you use?\n')
        i = 1
        for item in self.__attacks:
            print(str(i)+": "+item)
            i += 1
        print('')
        choice = int(input('Make a choice: '))
        return choice

    @staticmethod
    def dodge(dmg):
        rand = random.randint(0,100)
        if rand > 55:
            print('\n You failed to dodge! \n')
            return dmg
        else:
            print('\n You dodged successfully! \n')
            return 0

    def get_weapon_dmg(self):
        try:
            for i in self.__weapon:
                dmg = i.get_dmg(self.__atk)
                return random.randint(dmg - 10, dmg + 10)
        except:
            dmg = self.__weapon.get_dmg(self.__atk)
            return random.randint(dmg - 10, dmg + 10)

    def generate_damage(self, choice):
        dmg = random.randint(self.__atkl, self.__atkh)
        if not self.__fruit and not self.__weapon:
            if choice == 1:
                return dmg
            elif choice == 2:
                return dmg * self.__haki_attack
        if self.__fruit and not self.__weapon:
            if choice == 1:
                return dmg
            elif choice == 2:
                return dmg * self.__haki_attack
            elif choice == 3:
                return self.get_fruit_dmg()
            elif choice == 4:
                return self.get_fruit_dmg() * self.__haki_attack / 2
        if not self.__fruit and self.__weapon:
            if choice == 1:
                return dmg
            elif choice == 2:
                return dmg * self.__haki_attack
            elif choice == 3:
                return self.get_weapon_dmg()
            elif choice == 4:
                return self.get_weapon_dmg() * self.__haki_attack / 2
        if self.__fruit and self.__weapon:
            if choice == 1:
                return dmg
            elif choice == 2:
                return dmg * self.__haki_attack
            elif choice == 3:
                return self.get_fruit_dmg()
            elif choice == 4:
                return self.get_fruit_dmg() * self.__haki_attack / 2
            elif choice == 5:
                return self.get_weapon_dmg()
            elif choice == 6:
                return self.get_weapon_dmg() * self.__haki_attack / 2
        if choice not in range(1, len(self.__attacks) + 1):
            ch = int(input(f'That option is invalid, please enter a number between 1-{len(self.__attacks)}: '))
            return self.generate_damage(ch)


class Enemy(Person):
    def attack(self):
        choice = random.randint(1, len(self.__attacks))
        return self.generate_damage(choice)
