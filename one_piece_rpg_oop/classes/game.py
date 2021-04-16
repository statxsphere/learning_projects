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


devil_fruits = [{'name':'gomu', 'dmg':40, 'range':'long'},
                {'name':'mera', 'dmg':50, 'range':'medium'},
                {'name':'gura', 'dmg':80, 'range':'v_long'}]


def fruit_finder(x):
    for i in devil_fruits:
        if i['name'] == x:
            return i['dmg']


sword = {'good':40,'great':60,'supreme':80}


class Person:
    def __init__(self, hp, haki, hcost, atk, df, weapon=None, fruit=None):
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
        self.actions = ['Attack', 'Block', 'Dodge']
        self.attacks = ['Armament Haki', 'Melee', 'Weapon', 'Fruit']

    def generate_damage(self):
        if not self.weapon and not self.fruit:
            return random.randrange(self.atkl, self.atkh)

    def weapon_damage(self):
        try:
            dmg = sword[self.weapon]
            return random.randrange(dmg - 10, dmg + 10)
        except Exception:
            print('This character does not have a weapon')

    def fruit_damage(self):
        try:
            dmg = fruit_finder(self.fruit)
            return random.randrange(dmg - 10, dmg + 10)
        except Exception:
            print('This character does not have a devil fruit')

    def take_damage(self, dmg):
        self.hp -= dmg
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
