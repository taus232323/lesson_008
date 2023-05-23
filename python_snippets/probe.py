cat_names = ['Murzik', 'Tom', 'Vasya', 'Leo', 'Marta', 'Lokis', 'Ostin', 'Felix', 'Lucy', 'Elza']
cats = []
for cat in range(10):
    for name in cat_names:
        one_cat = Cat

        cat_names = ['Murzik', 'Tom', 'Vasya', 'Leo', 'Marta', 'Lokis', 'Ostin', 'Felix', 'Lucy', 'Elza']
        cats = []
        for name in cat_names:
            cat = Cat(house=home, name=name)
            cats.append(cat)