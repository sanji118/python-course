import random
#result = random.choice(['Head', 'Tail'])
#print(result)

side = random.randint(0, 1)
if side == 0:
    print('Head')
else:
    print('Tail')