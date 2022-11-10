from numpy import random
import random


def eGreedy(e: int):
    e = e / 100
    H1, H2, H3 = 10, 15, 12
    D1, D2, D3 = 8, 6, 5
    C1 = random.normalvariate(H1, D1)
    C2 = random.normalvariate(H1, D2)
    C3 = random.normalvariate(H3, D3)
    AvgC1, AvgC2, AvgC3 = 0, 0, 0
    count1, count2, count3 = 1, 1, 1
    cur_best = 0

    for day in range(297):
        cur_best = max(C1, C2, C3)

        x = random.random()

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
            cur_best = max(C1, C2, C3)
        else:
            if cur_best == C1:
                C1 += random.normalvariate(H1, D1)
                AvgC1 = C1 / count1
                count1 += 1
            elif cur_best == C2:
                C2 += random.normalvariate(H2, D2)
                AvgC2 = C2 / count2
                count2 += 1
            else:
                C3 += random.normalvariate(H3, D3)
                AvgC3 = C3 / count3
                count3 += 1
            cur_best = max(C1, C2, C3)

    return C1 + C2 + C3


eGreedy(30)

