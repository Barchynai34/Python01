#Условия if,else,elif.List -Списки
# number = int(input("Введите число:"))
# if number % 2== 0:
#     print(number, "Чётный")
# else :
#     print(number, "нечетный")

# age = int(input("Введите свой воззраст:"))
# if age < 13:
#     print("ВЫ не можете пользоваться нашей программой")
# elif age >= 13 and age <=40:
#     print("Добро пожоловать")
# else:
#     print("Error")

#Логические операторы or,and,in,not in
# Login = input("Login: ")
# password = input("Password: ")
# if Login == 'geeks' and password == 'geeks2023':
#     print("Welcome")
# else:
#     print("Incorrect login or password")

# word = "Geeks"
# Letter = "A"
# if Letter in word:
#     print(Letter,"есть в слове", word)
# else:
#     print(Letter,"нету в слове", word)

# names = 'Nurbolot Adilet Nursultan Beka'
# find_name = input("Find: ")
# if find_name not in names:
#     print(find_name,"не найден")
# else:
#     print(find_name,"найден")

#Lists - списки
#int, str, float ,bool, list
# name1 = 'Nurbolot'
# name2 = 'Kurmanbek'
# name3 = 'Askhat'
# name4 = 'Beksultan'

# names = ['Nurbolot', 'Kurmanbek', 'Askhat','Beksultan']
# print(names)
# print(names[2][0])
# print(names[1])
# print(names[1:3])
# print(names[::2])

# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(numbers)
# numbers.append(8)
# print(numbers)
# numbers.append(9)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# numbers[0] = 'one'
# print(numbers)
it_company  = ['Google', 'Meta', 'Microsoft']
# it_company.append('Tesla')
# print(it_company)
# it_company.insert(0, 'Geeks')
# print(it_company)
# it_company.pop(2)
# print(it_company)
print(it_company.index('Tesla'))

nums = [10, 1, 2, 212, 3, 4, 5, 11]
nums.sort()
print(nums)


numbers = [10, 100, 1000, 1, 2, 3, 4, 5, 50, 40, 11, 12, 22, 33, 44, 55]
print(min(numbers)) #Миниммальная значения
print(max(numbers)) #Максимальная значения
print(sum(numbers)) #Общая сумма
print(sum(numbers) / len(numbers)) #Среднее арифметическое значения