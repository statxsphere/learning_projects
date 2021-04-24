import random

class bcolors:
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
        self.name = name
        self.dmg = damage
        self.type = type
        self.spl = special
        self.immunity = True if self.type == "Logia" else False

    def get_dmg(self, attack):
        return attack + self.dmg


class DevilFruits:
    gomu = DevilFruit('gomu', 30, 'paramecia')


class Person:
    def __init__(self, hp, haki, hcost, atk, df, fruit=None, weapon=None):
        self.maxhp = hp
        self.hp = hp
        self.maxhaki = haki
        self.haki = haki
        self.haki_attack = hcost
        self.atk = atk
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.weapon = weapon
        self.fruit = fruit
        self.fruit_attack = self.fruit.get_dmg(self.atk) if fruit else None
        self.actions = ['Attack', 'Block', 'Dodge']
        self.attacks = ['Melee', 'Busoshoku', 'Devil Fruit', 'Haki Devil Fruit']

    def get_fruit_dmg(self):
        return random.randint(self.fruit_attack - 10, self.fruit_attack + 10)

    def take_damage(self, dmg):
        self.hp -= dmg/self.df
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_haki(self):
        return self.haki

    def get_maxhaki(self):
        return self.maxhaki

    def take_haki(self, haki_used):
        self.haki -= haki_used

    def get_devil_fruit(self):
        return self.fruit

    def get_haki_cost(self):
        return self.haki_attack

    def choose_action(self):
        i = 1
        for item in self.actions:
            print(str(i)+": "+item)
            i += 1

    def choose_attack(self):
        i = 1
        for item in self.attacks:
            print(str(i)+": "+item)
            i += 1
        choice = int(input('Make a choice: '))
        return choice

    def generate_damage(self, choice):
        dmg = random.randint(self.atkl, self.atkh)
        if choice == 1:
            return dmg
        elif choice == 2:
            return dmg * self.haki_attack
        elif choice == 3:
            return self.get_fruit_dmg()
        elif choice == 4:
            return self.get_fruit_dmg() * self.haki_attack/2
        else:
            ch = int(input('that option is invalid, please enter a number between 1-4: '))
            return self.generate_damage(ch)


class Enemy(Person):
    def __init__(self, hp, haki, hcost, atk, df, fruit=None, weapon=None):
        super().__init__(hp, haki, hcost, atk, df, fruit=None, weapon=None)

    def attack(self):
        choice = random.randint(1, 4)
        self.generate_damage(choice)
