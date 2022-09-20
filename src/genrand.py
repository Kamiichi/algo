import random

Num = 10

rand_list = [] * Num

for i in range(Num):
    rand_list.append(random.randint(1,100))

print(*rand_list)
sorted_list = sorted(rand_list)