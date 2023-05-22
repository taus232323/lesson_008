# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.


class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.fur_coat = 0
        self.money_earned = 0
        self.food_eaten = 0

    def pollution(self):
        self.dirt += 5

    def __str__(self):
        return 'In the house left: {} money, {} food, {} dirt, {} fur coat. {} money earned, {} food eaten'. \
            format(self.money, self.food, self.dirt, self.fur_coat, self.money_earned, self.food_eaten)


class Man:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30
        self.happiness = 100

    def act(self):
        if self.fullness == 0:
            cprint('{} died of starvation.'.format(self.name), color='red')
            return
        elif self.happiness == 0:
            cprint('{} died of depression.'.format(self.name), color='red')
            return
        if self.house.dirt > 100:
            self.happiness -= 10
            cprint('it is dirty in the house', color='red')

    def __str__(self):
        return 'I am {}, my happiness is {} and fullness is {}'.format(self.name, self.happiness, self.fullness)


class Husband(Man):
    def __int__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 4)
        if self.house.money <= 30:
            self.work()
        elif self.fullness <= 20:
            self.eat()
        elif self.happiness <= 20:
            self.gaming()
        else:
            if dice == 1 or 3:
                self.work()
            elif dice == 2:
                self.eat()
            else:
                self.gaming()

    def eat(self):
        if self.house.food > 20:
            cprint('{} ate'.format(self.name), color='green')
            meal = randint(20, 30)
            self.house.food -= meal
            self.fullness += meal
            self.house.food_eaten += meal
        else:
            cprint('there is not enough food in the house', color='red')

    def work(self):
        if self.fullness > 10 and self.happiness > 10:
            cprint('{} went to work'.format(self.name), color='grey')
            self.house.money += 150
            self.fullness -= 10
            self.happiness -= 10
            self.house.money_earned += 150
        else:
            cprint('{} tired'.format(self.name), color='red')
            self.eat()

    def gaming(self):
        if self.fullness > 20:
            cprint('{} played WoT the whole day'.format(self.name), color='blue')
            self.happiness += 20
            self.fullness -= 10
        else:
            cprint('{} is hungry'.format(self.name), color='red')
            self.eat()


class Wife(Man):
    def __int__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 5)
        if self.house.food <= 20:
            self.shopping()
        elif self.fullness <= 20:
            self.eat()
        elif self.happiness <= 20:
            self.buy_fur_coat()
        elif self.house.dirt >= 80:
            self.clean_house()
        else:
            if dice == 1:
                self.buy_fur_coat()
            elif dice == 2:
                self.eat()
            elif dice == 3:
                self.clean_house()
            else:
                self.shopping()

    def eat(self):
        if self.house.food > 20:
            cprint('{} ate'.format(self.name), color='green')
            meal = randint(20, 30)
            self.house.food -= meal
            self.fullness += meal
            self.house.food_eaten += meal

        else:
            cprint('there is not enough food in the house', color='red')
            self.shopping()

    def shopping(self):
        if self.house.money > 30:
            shop = randint(20, 30)
            self.house.food += shop
            self.house.money -= shop
            cprint('{} went to shop and bought {} food'.format(self.name, shop), color='yellow')
        else:
            cprint('there is not enough money in the house', color='red')
            self.clean_house()

    def buy_fur_coat(self):
        if self.house.money > 400 and self.fullness > 20:
            cprint('{} bought fur coat'.format(self.name), color='blue')
            self.house.fur_coat += 1
            self.house.money -= 350
        else:
            cprint('there is not enough money for buy fur coat', color='red')
            self.eat()

    def clean_house(self):
        if self.fullness >= 20 and self.happiness >= 10:
            max_cleaning = 100
            cleaning = min(max_cleaning, self.house.dirt)
            self.house.dirt -= cleaning
            cprint('{} cleaned the house'.format(self.name), color='grey')


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)


for day in range(365):
    print('================== День {} =================='.format(day))
    serge.act()
    masha.act()
    home.pollution()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='magenta')


# после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья - не меняется, всегда ==100 ;)

class Child(Man):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.fullness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 2)
        if self.fullness < 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()

    def eat(self):
        if self.house.food > 10:
            cprint('{} ate'.format(self.name), color='green')
            food = randint(5, 10)
            self.house.food -= food
            self.fullness += food
        else:
            cprint('there is not enough food in the house', color='red')

    def sleep(self):
        if self.fullness > 10:
            cprint('{} slept'.format(self.name), color='green')
            self.fullness -= 10
        else:
            cprint('{} is hungry'.format(self.name), color='red')
            self.eat()


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
