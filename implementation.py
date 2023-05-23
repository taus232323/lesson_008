# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint
from family import House, Husband, Wife, Child, Cat


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
cat_names = ['Murzik', 'Tom', 'Vasya', 'Leo', 'Marta', 'Lokis', 'Ostin', 'Felix', 'Lucy', 'Elza', 'Lois',
             'Meicy', 'Alta', 'Beth', 'Vikki', 'Gerta', 'Sima', 'Wendy', 'Gary', 'Lux']
cats = []
for i in range(2):
    cat_name = cat_names[randint(0, len(cat_names)-1)]
    cat = Cat(house=home, name=cat_name)
    cats.append(cat)
for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    if randint(0, 365) < 6:
        home.money_incident()
    if randint(0, 365) < 6:
        home.food_incident()
    serge.act()
    masha.act()
    kolya.act()
    for one_cat in cats:
        one_cat.act()
    home.pollution()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    for one_cat in cats:
        cprint(one_cat, color='cyan')
    print(home)
