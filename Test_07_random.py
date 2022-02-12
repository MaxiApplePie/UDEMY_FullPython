import random

for i in range (5):
    r = random.randint(0, 10)
    print(r)

a = random.randint(30)
b = random.randint(30)
if b > a:
    print('Le nombre b est plus grand que le nombre a .')
else:
    print('Le nombre a est plus grand que le nombre b.')
