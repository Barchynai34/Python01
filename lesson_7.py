# def hello_world(name:str):
#     print("Hello World and Hello", name)
# hello_world("Nurbolot")

# def div(num1:int=1, num2:int=1) -> float:
#     return num1 / num2
# print(div(10, 5))

# def reverse_name(name:str="Alihan") -> str:
#     return name[::-1]
# # print(reverse_name())
# # print(reverse_name("Nurbolot"))

# def hello(word:str="Python") -> str:
#     print("Geeks")
#     print("Hello")
#     return "Alihan"
# hello()

# def calculator(num1:int=1, operator:str="+", num2:int=1) -> int:
#     "Базовая функция калькулятора на Python"
#     if operator =="+":
#         return num1 + num2
#     elif operator =="-":
#         return num1 - num2
#     elif operator =="*":
#         return num1 * num2
#     elif operator =="/":
#         return num1 / num2
#     else:
#         return "Такого оператора нету"
# print(calculator(10, "*", 10))   
# print(calculator(10, "/", 3)) 
# print(calculator(1, "Alihan", 2)) 

#Args,kwargs
# print('Hello', 'World', 'and','Python')

# def welcome(name,name2, name3):
#     print("Добро пожоловать", name)
#     print("Добро пожоловать", name2)
#     print("Добро пожоловать", name3)
# welcome('Nurbolot','Alihan','Kurmanbek')

def args_welcome(*args):
    for name in args:
        print("Добро пожаловать", name)
args_welcome('Nurbolot','Alihan','Kurmanbek', 'Beksultan')
