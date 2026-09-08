height= int(input('your height='))
if height >= 3 :
    print('You can ride.')
    age = int(input('your age='))
    if age< 12:
        bill= 150
        print('Please pay 150 tk')
    elif age <= 18:
        bill= 250
        print('Please pay 250 tk')
    else:
        bill= 500
        print('please pay 500 tk')
    want_photo= input('Do you want to take photo?(Y/N)')
    if want_photo == 'Y':
            bill = bill + 50
    print(f'Your total bill is {bill}')
else:
    print('you can not ride')
print('THANK YOU')