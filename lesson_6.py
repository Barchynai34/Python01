#Функции - functions
# print('Geeks')
# def hello_world():
#     print("Hello_World")
# #hello_world()

# def add():
#     num1 = int(input("Number1: "))
#     num2 = int(input("Number: "))
#     print(num1+num2)
# add()

# def count_numbers():
#     numbers = [1,2,3,4,5,6,7,8,9,10]
#     for number in numbers:
#         if number % 2  == 0:
#             print(number, "Четный")
#     else:
#         print(number, "Нечетный")   
# count_numbers()   

# def revers_word(word):
#     print(word[::-1])
# revers_word("Geeks") 
# revers_word("Python")  
# revers_word("Django")

# def hello(name):
#     print("Привет", name)
# hello("Kurmanbek")
# hello("Beksultan")

# def test(word:str) -> str:
#     "My testing function geeks"
#     print(word+word)
# test("geeks")    
# test(10)


# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Деление на ноль")

# try:
#     print(10 + 10)
# except BaseException:
#     print("Code Error")

while True:
    try:
        person = int(input("question: "))
    except ValueError:
        print("Конечно!")
        # operator = input("Operator: ")
        if person == "Вот так!":
            print("Успакойся ")
        elif person == "?":
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        # elif operator == "*":
        #     print("Ответ: ", num1 * num2)
        # elif operator == "/":
            # try:

            # except ZeroDivisionError:       
        else:
            print("“ну и что”")
    # except ValueError:
    #     print("Конечно!")
