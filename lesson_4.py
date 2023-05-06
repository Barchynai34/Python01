#Tuple - Кортежи. Циклы for и while
#int, float, bool, str, tuple - неизм.
#List - изм

# names = ('Kurmanbek','Beksultan','Nurbolot')
# print(names)
# print(names[0])
# print(names[1:3])
# print(names[::2])

# names.append('Askhat')
# print(names)

# # names.pop(0)
# names.remove('Nurbolot')
# names[0] = "python"

# ist = ['Hello']
# print(type(ist))

# tup = ('Hello',)
# print(type(tup))

# tup = ('Hello',10, 0.1, True, [1,2,3,4],(1,2,3,4))
# print(tup)
# print(tup[4][0])

# cars = ('BMW', 'Mersedes', 'Audi')
# print(cars)
# lst_cars = list(cars)
# print(lst_cars)
# lst_cars.append('Tesla')
# cars = tuple(lst_cars)
# print(cars)

# import dis
# lst = [1,2,3,4,5]
# lst.append(10)
# tup  = (1,2,3,4,5)

# # dis.dis('lst')
# dis.dis('tup)

#Циклы for, while
#print(1)
#print(2)
#print(9)

# for num in range(1001):
#     print(num,'Geeks')

# for i in range(10,50):
#     print(i)

# for i in range(10000001):
#     print(i)

# numbers = [10, 11, 100, 333, 445, 34, 45, 67, 2, 101, 102]
# for n in  numbers:
#     if n % 2 ==0:
#         print(n,"Четный")
#     else:
#         print(n,"Нечетный")

# it = ["Geeks", "Meta", "Google", "Neobis"]
# for i in it:
#     print(i)
#     if i =="Meta":
#         break #break досрочно прерывает цикл, contunie - продолжать цикл

# name = "Nurbolot"
# for n in name:
#     print(n)

# num1 = 10
# # num2 = 20
#  num1 < num2: #Цикл 
#     num1 +=1
#     #num1 = num1 + 1
#     print(num1)

# n = 0
# while True:
#     n += 1
#     print('Geeks',n)

# while True:
#     num1 = int(input("Number1: "))
#     operator = input("+, -, *, /: ")
#     num2  = int(input("Number2: "))
#     if operator == "+":
#         print("Ответ: ",num1 + num2)
#     elif operator == "-": 
#         print("Ответ: ",num1 - num2)  
#     elif operator == "*":
#         print("Ответ: ",num1 * num2)
#     elif operator == "/": 
#         print("Ответ: ",num1 / num2)
#     elif num1 == 0 and num2 == 0 and operator =="0":
#         print("Stop")
#         break
#     else:
#         print("Тлько оператор не существует")

# import random

# # print(random.randint(1, 10))

# random_number = random.randint(1,10)
# attempt = 0
# while True:
#     input_number = int(input("Введите от 1 до 10: "))
#     if input_number >= 1 and input_number <= 10:
#         attempt += 1
# # attempt  += 1
#         if attempt ==5:
#            print("Вы проиграли")
#            break
#         elif input_number == random_number:
#             print("Вы выиграли! Поздравляем!")
#             break
#         else:
#              print("Неправильно у вас", 5 - attempt, "попыток")

# print("Сколько бананов и ананасов для обезьян?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")
# print("Сколько жуков и червей для ежей?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")
# print("Сколько рыб и моллюсков для выдр?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")

def cylinder():
    try:
        r = float(input())
        h = float(input())
    except ValueError:
     return
    side = 2 * 3.14 * r * h
    circle = 3.14 * r**2
    full = side + 2 * circle
    return full
print(cylinder(56))