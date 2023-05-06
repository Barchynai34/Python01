#Задача №1
# for i in range(0,5):
#     print(i+1,'0')

#Задача №2
# for i in range(1,101):
#     print(i)

#Задача №3
# a = [i for i in range(497) if i % 2 == 0]
# print(a)

# Задача №4
a = range(1, 1000)
m = (min(a))
m = (max(a))
m = (sum(a))
print(m)

#Задача №5




#Задача №6
it_company = ('Google', 'Amazon', 'Microsoft')
# print(it_company)
# lst_it_company = list(it_company)
# print(lst_it_company)
# lst_it_company.append('Tesla')
# it_company = tuple(lst_it_company)
# print(it_company)

#print(it_company.index('Amazon')) #задача№7
result_company = [elem.replace('Google','Apple')for elem in it_company]
print(result_company[0:3]) #Задача№8 и 9





text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
'overview') 
str_cnt = text_tuple.count('Python')
print(str_cnt)

#Доп.задача
# a = 1
# b =2
# print(a,b)
# a,b = b,a
# print(a,b)
# a = int(input('Введите первое число:'))
# b = int(input('Ввведите второе число: '))
# a,b = b,a
# print(a)
# print(b)

# age = int(input("Ввыведите возраст:"))
# if age <18:
#     print("Извините, пользование данным ресурсом только с 18 лет")
# elif age >= 18:
#     print("Доступ разрешен")