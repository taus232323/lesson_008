def eat(self):
    if self.house.food > 20:
        meal = randint(20, 30)
        self.house.food -= meal
        self.fullness += meal
        cprint('{} ate'.format(self.name), color='green')
    else:
        cprint('{} there is not enough food in the house'.format(self.name), color='red')
        self.work()