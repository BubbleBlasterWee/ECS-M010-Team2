import random


def exploreOnly():
    happiness = 0
    for i in range(100):  # loops for all 300 days; only 100 because we add to happiness 3 times in the for loop, and 300/3=100
        happiness = happiness + random.normalvariate(10, 8)  # adds C1
        happiness = happiness + random.normalvariate(15, 6)  # adds C2
        happiness = happiness + random.normalvariate(12, 5)  # adds C3
    return happiness
