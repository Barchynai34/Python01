#Задача №1
# def shorter(word):
#     word_dict = word.split()
#     for i in range(len(word_dict)):
#         print(word_dict[i][0], end = '')
# shorter('Кыргыз Республикасы')       

#Задача №2
#Задача №3
# def text(word):
#     word_dict = list(word)
#     no_duble = set(word)
#     if len(word_dict) == len(no_duble):
#         print("True")
#     else:
#         print("False")

# text(input("Введите слова: "))

# #Задача №4
# def reverse_num(number):
#     print(number[::-1])
# reverse_num("923")


# Доп.задание
# n = input("Введите: ")
# while type(n) = int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Конечно!")
#     if n == "Вот так!":
#         print("Успокойся!")

def chatbot():
    while True:
        text=input("Введите что-то:")
        if text.find("?")>=0:
            print("Конечно!")
        elif text.find("!")>=0:
            print("Успокойся")
        elif text == "":
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        else:
            print("Ну и что")
chatbot()
        