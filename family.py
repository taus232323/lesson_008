# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30
        self.fur_coat = 0
        self.money_earned = 0
        self.food_eaten = 0
        self.money_lost = 0
        self.food_lost = 0
        self.money_lost_times = 0
        self.food_lost_times = 0

    def money_incident(self):
        lost = self.money / 2
        self.money -= int(lost)
        cprint('Family just has lost {} money'.format(lost), color='red')
        self.money_lost += int(lost)
        self.money_lost_times += 1

    def food_incident(self):
        lost = self.food / 2
        self.food -= int(lost)
        cprint('Family just has lost {} food'.format(lost), color='red')
        self.food_lost += int(lost)
        self.food_lost_times += 1

    def pollution(self):
        self.dirt += 5

    def __str__(self):
        return 'In the house left: {} money, {} food, {} dirt, {} cat food, {} fur coat.\n' \
               '{} money earned, {} food eaten.\nThere were {} times {} money lost and {} times {} food lost'. \
            format(self.money, self.food, self.dirt, self.cat_food, self.fur_coat,
                   self.money_earned, self.food_eaten, self.money_lost_times, self.money_lost, self.food_lost_times,
                   self.food_lost)


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

    def buy_cat_food(self):
        if self.house.money > 30:
            shop = randint(20, 30)
            self.house.cat_food += shop
            self.house.money -= shop
            cprint('{} bought cat food'.format(self.name), color='yellow')
        else:
            cprint('there is not enough money in the house', color='red')

    def pet_the_cat(self):
        if self.fullness > 20:
            cprint('{} petted the cat'.format(self.name), color='blue')
            self.happiness += 5
            self.fullness -= 10
        else:
            cprint('{} is hungry'.format(self.name), color='red')
            return

    def __str__(self):
        return 'I am {}, my happiness is {} and fullness is {}'.format(self.name, self.happiness, self.fullness)


class Husband(Man):
    def __int__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 6)
        if self.house.money <= 30:
            self.work()
        elif self.fullness <= 20:
            self.eat()
        elif self.happiness <= 20:
            self.gaming()
        elif self.house.cat_food <= 20:
            super().buy_cat_food()
        else:
            if dice == 1 or 3:
                self.work()
            elif dice == 2:
                self.eat()
            elif dice == 4:
                super().pet_the_cat()
            elif dice == 5:
                super().buy_cat_food()
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
            self.house.money += 400
            self.fullness -= 10
            self.happiness -= 10
            self.house.money_earned += 400
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
        dice = randint(1, 6)
        if self.house.food <= 20:
            self.shopping()
        elif self.fullness <= 20:
            self.eat()
        elif self.happiness <= 20:
            self.buy_fur_coat()
        elif self.house.dirt >= 80:
            self.clean_house()
        elif self.house.cat_food <= 20:
            super().buy_cat_food()
        else:
            if dice == 1:
                self.buy_fur_coat()
            elif dice == 2:
                self.eat()
            elif dice == 3:
                self.clean_house()
            elif dice == 4:
                super().buy_cat_food()
            elif dice == 5:
                super().pet_the_cat()
            else:
                self.shopping()

    def eat(self):
        if self.house.food > 20 and self.fullness < 100:
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


class Cat:

    def __init__(self, house, name):
        self.house = house
        self.name = name
        self.fullness = 30

    def act(self):
        if self.fullness == 0:
            cprint('{} died of starvation.'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.soil()

    def eat(self):
        if self.house.cat_food > 10:
            cprint('{} ate'.format(self.name), color='green')
            food = randint(5, 10)
            self.house.cat_food -= food
            self.fullness += food * 2
        else:
            cprint('there is not enough cat food in the house', color='red')
            self.sleep()

    def sleep(self):
        if self.fullness > 10:
            cprint('{} slept'.format(self.name), color='blue')
            self.fullness -= 10
        else:
            cprint('{} is hungry'.format(self.name), color='red')

    def soil(self):
        if self.fullness > 10:
            cprint('{} spoilt wallpapers'.format(self.name), color='grey')
            self.house.dirt += 5
            self.fullness -= 10
        else:
            cprint('{} is hungry'.format(self.name), color='red')
            self.eat()

    def __str__(self):
        return 'I am {}, my fullness is {}'.format(self.name, self.fullness)


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
