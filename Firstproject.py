print("Welcome")
for x in range(3):
    print(x)
print('Kuet')
a = 10
b = 20
c = a+b
print(c)
print('print("what to print")')
print("hello world\n hello world \n hello world")
print("hello"+"world")
print("hello world \t hello world")

name = input("What is your name?")
print(f'Hello, {name}!')
print('hey'+input("What is your name?")+','+' how are you?')
name = input("What is your name?")
length = len(name)
print(length)
name_1 = "Dark chocolate"
name_2 = "Sanjida"
print(name_1[5])
print(name_1 + name_2)
print(7*"I hate you")
a = input("enter th value=")
b = input("enter the value =")
print(int(a)+int(b))
number = input("enter a two digit number:")
first_digit = number[0]
second_digit = number[1]
print(int(first_digit)+int(second_digit))
a,b = 5,4
print(a>4 and b<10)
print(a>4 or b>10)
a = 5
b= 5
print(a & b)
print(a | b)
print(a ^ b)
print(~b)
print(a << b)
print(a >> b)
a=10
b=10
print(a is b)
print(a is not b)
a=10
print(id(a))
a=9
print(id(a))
print(a is a)
str='Dark chocolate'
print('y' in str)
print('r' not in str)
print('choco' in str)
l1=[1,10,-5.2]
print(0 in l1)
print(-5 in l1)
weight=input('enter weight in kg:')
height = input('enter height in meter:')
BMI = int(weight)/float(height) ** 2
print(BMI)