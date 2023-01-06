def cZodiac(date):
    zodiac = ''
    nums = '1 2 3 4 5 6 7 8 9 10 11 12'.split()
    animals =' Rooster Dog Pig Rat Oxen Tiger Rabbit Dragon Snake Horse Sheep Monkey'.split()
    zodiac = (date%12) - 1
    zodiac = animals[zodiac]
    print(zodiac)
