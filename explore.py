import random


def exploreOnly():
    happiness = 0
    for i in range(100):
        happiness = happiness + random.normalvariate(10, 8)
        happiness = happiness + random.normalvariate(15, 6)
        happiness = happiness + random.normalvariate(12, 5)
    return happiness
