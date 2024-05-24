import random

num = random.randrange(3,21)
parol = []
print(num)
for i in range(1, 20):
    for j in range(2, 21):
        sum = i + j
        if sum <= num and num % sum == 0 and i < j:
            list = [i, j]
            parol.extend(list)
print(*parol, sep='')

i = 1
parol_1 = []
while i < num:
    j = 2
    while j <= num:
        sum_1 = i + j
        list_1 = [i, j]
        if sum_1 <= num and num % sum_1 == 0 and i < j:
            parol_1.extend(list_1)
        j += 1
    i += 1
print(*parol_1, sep='')





    