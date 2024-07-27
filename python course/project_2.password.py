import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers =['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['\\', '/' ,':' ,'*', '?', '"', '<', '>', '|', '&', '$', '@', '#']
print("Welcome to Password Generator!")
letters_num = int (input("How many letters you waant in your password?\n"))4
numbers_num = int (input("How many numbers you waant in your password?\n"))
symbols_num = int (input("How many symbols you waant in your password?\n"))
password= " "
for i in range(1 , letters_num+1):
    char = random.choice(letters)
    password = password + char
for i in range(1 , numbers_num+1):
    num = random.choice(numbers)
    password = password + num
for i in range(1 ,symbols_num+1):
    sym = random.choice(symbols)
    password = password + sym
print(password)