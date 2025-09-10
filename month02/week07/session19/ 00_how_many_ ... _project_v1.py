import random


def life_in_weeks(age):

    year_remaining = 90 -age
    week_remaining = year_remaining*52

    
    print((f" week left for you:{week_remaining}"))

life_in_weeks(43)
# output: You have 2444 weeks left.
life_in_weeks(56)
# output: You have 1776 weeks left.
life_in_weeks(12)
# output: You have 4036 weeks left.