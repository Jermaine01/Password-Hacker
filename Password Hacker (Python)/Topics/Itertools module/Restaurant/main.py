import itertools

for main, dess, pri, in itertools.product(price_main_courses, price_desserts, price_drinks):

    if main + dess + pri <= 30:
        print(main_courses[price_main_courses.index(main)], end=' ')
        print(desserts[price_desserts.index(dess)], end=' ')
        print(drinks[price_drinks.index(pri)], end=' ')
        print(main + dess + pri)
