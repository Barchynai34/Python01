#Задача №1
password = input("Passworrd: ")
if password == "geeksstudents":
    print("Password is correct.You're welcome")
else:
    print("Password is incorrect.Please,try again")


Login = input("Login: ")
password = input("Password: ")
if password == "geeksstudents":
    if Login == "geeks":
        print("Welcome")
    else:
        print("Incorrect Login")
else:
    print("Password is incorrect. Please, try again")


#Задача №2

# temperature = int(input("Погода:"))
# if temperature == -30:
#    print("Там так холодно, лучше дома сиди!")

# elif  temperature in range(-30, 0):
#     print("Холодновато. Оденься потеплее!")


# elif  temperature in range(0, 15):
#      print("Прохладно. Куртку накинь!")

# elif temperature in range(15, 30):
#     print("Тепло. Иди погуляй в парке!")

# elif temperature in range(30, 50):
#     print("Ого, как жарко!")

# elif temperature > 50:
#     print("Там такая жара, лучше сиди дома!")

# else:
#     print("Ошибка!")




#Задача  №3
# string = "Advertising companies say advertising is necessary and important. It informs people about
# new products. Advertising hoardings in the street make our environment colourful. And
# adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
# programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
# healthy products. And adverts in magazines give us ideas for how to look prettier, be
# fashionable and be successful. Without advertising, life is boring and colourless.
# But some consumers argue that advertising is a bad thing. They say that advertising is bad
# for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
# know we love our children and want to give them everything. So they use children’s ‘pester
# power’ to sell their products. Finally, consumers say, if there is advertising there must be
# rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
# money"

# start = string.find("s")
# start = string.find("t")


#Доп.задача

str1 = 'Aidana'

str2 = 'Adilet'

new_str =''

for i in range(6):

    new_str += str1[i] + str2[i]

print(new_str)