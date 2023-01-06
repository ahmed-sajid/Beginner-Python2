def cZodiac(date):
    nums = '1 2 3 4 5 6 7 8 9 10 11 12'.split()
    animals =' Rooster Dog Pig Rat Oxen Tiger Rabbit Dragon Snake Horse Sheep Monkey'.split()
    x = 12
    y = 0
    for i in range(12):
        if date%x == 0:
            zodiac = animals[y]
            print(zodiac)
            x = x - 1
            x = y + 1
    print(zodiac)
cZodiac