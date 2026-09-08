size= input('What size pizza you want?(S/M/L)')
bill = 0
if size == 'S' or size=='s':
    print('Small size pizza is 200 tk')
    bill += 200
if size == 'M' or size=='m':
    print('Medium size pizza is 300 tk')
    bill += 300
else:
    print('Large size pizza is 500 tk')
    bill += 500
add_pepperoni = input('Do you want to add pepperoni?(Y/N)')
if add_pepperoni == 'Y':
    if size == 's' or size == 'S':
       bill += 30
    else:
        bill += 40
add_cheese= input('Do you want to add cheese? ( Y/N)')
if add_cheese == 'Y':
    if size =='S' or size=='s':
       bill+=50
    else:
        bill+=60
add_mushroom = input('Do you want to add mushroom?(Y/N)')
if add_mushroom== 'Y':
    if size =='S' or size=='s':
        bill += 35
    else:
        bill += 45
print(f'Your bill is {bill}')
print('Thank you for purchasing:)')