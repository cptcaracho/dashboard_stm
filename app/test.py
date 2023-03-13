import random

cost = round(random.uniform(200, 400), 2)
revenue = round(random.uniform(100, 700), 2)
profit = round(revenue - cost, 2)
roi = round((revenue - cost) / cost * 100, 2)

print(cost)
print(revenue)
print(profit)
print(roi)
nr = 1
a = 'campaign'

print(a + str(nr))
