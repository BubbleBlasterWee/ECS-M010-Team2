import random


def eGreedy(e=10: int):
    # turn e into a float
    e = e / 100
    # setting up the initial values of three cafeterias(each vist once)
    H1, H2, H3 = 10, 15, 12
    D1, D2, D3 = 8, 6, 5
    C1 = random.normalvariate(H1, D1)
    C2 = random.normalvariate(H2, D2)
    C3 = random.normalvariate(H3, D3)
    # keep track of the average, day counts, and the current best cafeteria
    AvgC1, AvgC2, AvgC3 = 0, 0, 0
    count1, count2, count3 = 1, 1, 1
    cur_best = 0

    # loop for the next 297 days, always update current best cafeteria
    for day in range(297):
        cur_best = max(AvgC1, AvgC2, AvgC3)
        
        # generates a float smaller than 1 bigger than 0
        x = random.random()
        
        # choose a random cafeteria based on random number generator i
        if x <= e:
            i = random.randint(1, 3)
            if i == 1:
                C1 += random.normalvariate(H1, D1)
                AvgC1 = C1 / count1
                count1 += 1
            elif i == 2:
                C2 += random.normalvariate(H2, D2)
                AvgC2 = C2 / count2
                count2 += 1
            else:
                C3 += random.normalvariate(H3, D3)
                AvgC3 = C3 / count3
                count3 += 1
        # go to the current best cafeteria
        else:
            if cur_best == AvgC1:
                C1 += random.normalvariate(H1, D1)
                AvgC1 = C1 / count1
                count1 += 1
            elif cur_best == AvgC2:
                C2 += random.normalvariate(H2, D2)
                AvgC2 = C2 / count2
                count2 += 1
            else:
                C3 += random.normalvariate(H3, D3)
                AvgC3 = C3 / count3
                count3 += 1

    return C1 + C2 + C3

