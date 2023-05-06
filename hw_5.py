#Задача №1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd':600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

#Задача №2
# numbers = {'num_1' : 1, 'num_2' : 2,'num_3' : 3, 'num_100' : 100}
# result = 5
# for key in numbers:
#     result =result * numbers[key]
#     print(result)

#Задача №3
# student = {'name' : 'Askhat', 'age' : 17}
# print(student['age']*2)

#Задача №4
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# print("Initial Dictionary: ", student)
# student['age'] = 16
# print("Initial Dictionary: ", student)

#Задача №5
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)

#Задача №6
# student = {'name' : 'Askhat'}
# student['address'] = 'Западный Анар'
# print(student)


#Доп.задача №7
# while True:
#     password1 = input("password 1: ")
#     password2 = input("password 2: ")
#     a = True
#     if len(password1)<8:
#         a = False
#         print("Короткий пароль!")
#     elif "1234567890" in password1:
#         a = False
#         print("Простой пароль!")       
#     elif password1 != password2:
#         a = False
#         print("Разлечаются")
      
#     else:
#         break
# print("OK","Пароль создан!")