weight = float(input('enter weight in kg='))
height = float(input('enter height in meter='))
bmi= weight/height ** 2
if bmi < 18.5:
    print(f'your bmi is {bmi} and you are underweight.')
elif bmi < 25:
        print(f'your bmi is {bmi} and you are normal weight.')
elif bmi < 30:
        print(f'your bmi is {bmi} ND YOU are overweight.')
else:
  print(f'you are obese.')

