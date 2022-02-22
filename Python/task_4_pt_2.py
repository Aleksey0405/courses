# Задание 4_part_2
# Предусловие.
# Задачи 3 и 4 выполнить в 2-х вариантах:
# 1) В процедурном виде (весь код в одной процедуре).
# 2) В виде функций - код разбит на функции. Отдельные функции можно вынести в другие .py файлы и вызывать их в main.py предвварительно импортируя в main.py.


# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться. 
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.

input_data = int(input("Enter BYN"))
byn_to_usd = input_data / 2.63
print ("Ты ввел ", input_data, "BYN")
print ("Конвертировання сумма в USD = ", byn_to_usd, 'USD')            

# Задача №2  
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться. 
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.
currency = ["EUR", "USD", "CHF", "GBP", "CNY", "RUB"]
rate_currency = [1, 1.1138, 1.0378, 0.8318, 7.0857, 86.6113]

target_currency = currency[0]
target_currency_amount = int(input("Введи количество евро: "))
print("Ты ввёл", target_currency_amount, target_currency)
currency_result = 0

for a in range(len(currency)):
    currency_result = round(target_currency_amount * rate_currency[a])
    print("Конвертированная сумма в", currency[a], "=", currency_result)


# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться. 
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
    
#     3. Скипт должен выдать сообщение 
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     4. Валюту пользователя определите сами.
# Задача 3 вариант 1
currency = ["EUR", "USD", "CHF", "GBP", "CNY", "RUB"]
rate_currency = [1, 1.1138, 1.0378, 0.8318, 7.0857, 86.6113]

target_currency = currency[0]
target_currency_amount = input("Введи количество евро: ")

try:
    target_currency_amount = int(target_currency_amount)
    it_is_integer = True
except ValueError:
    it_is_integer = False

if target_currency_amount == '':
    print("Вы ввели пустое поле. Введите число.")

elif it_is_integer:
    if target_currency_amount>0:
        print("Ты ввёл", target_currency_amount, target_currency)
        currency_result = 0

        for a in range(len(currency)):
            currency_result = target_currency_amount * rate_currency[a]
            print("Конвертированная сумма в", currency[a], "=", currency_result)

    else:
        print("Введите положительное число.")

else:
    print("Вы ввели не число. Введите число.")

# Задача 3 вариант 2
def emptiness_check(var):
    if var == '':
        return True
    else:
        return False


def integer_check(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


def pos_check(var):
    if int(var) > 0:
        return True
    else:
        return False


def currency_conv(amount, currency, rate):
    output_list = []
    for a in range(len(currency)):
        currency_result = round(int(amount) * rate[a])
        output_list.append("Конвертированная сумма в " + currency[a] + " = " + str(currency_result))
    return output_list


currency = ["EUR", "USD", "CHF", "GBP", "CNY", "RUB"]
rate_currency = [1, 1.1138, 1.0378, 0.8318, 7.0857, 86.6113]

target_currency_amount = input("Введи количество евро: ")

if emptiness_check(target_currency_amount):
    print("Вы ввели пустое поле. Введите число.")
elif not integer_check(target_currency_amount):
    print("Вы ввели не число. Введите число.")
elif not pos_check(target_currency_amount):
    print("Введите положительное число.")
else:
    amount_list = currency_conv(target_currency_amount, currency, rate_currency)
    for a in amount_list:
        print(a)



                
# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение 
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.

#Вариант1
currency = ["EUR", "USD", "CHF", "GBP", "CNY", "RUB"]
rate_currency = [1, 1.1138, 1.0378, 0.8318, 7.0857, 86.6113]

while True:
    target_currency_position = None
    print("Выберите валюту из", currency)
    target_cur_name = input()

    for i in range(len(currency)):
        if currency[i].lower() == target_cur_name.lower():
            target_currency_position = i

    if target_currency_position is None:
        print("Введите валюту из списка")
        continue

    target_currency_amount = input("Введите сумму в EUR: ")  
    
    if target_currency_amount == '':
        print("Вы ввели пустое поле. Введите число.")
    
    try:
        target_currency_amount = int(target_currency_amount)
        it_int = True
    except ValueError:
        it_int = False
    
    if it_int:
        if target_currency_amount > 0:  
            print("Вы ввели сумму", target_currency_amount, currency[0])

            currency_result = round(target_currency_amount * rate_currency[target_currency_position])
            print("Конвертированная сумма в", currency[target_currency_position], "=", currency_result)
        else:
            print("Введите положительное число.")
    else:
        print("Вы ввели не число. Введите число.")

#Вариант 2
def empty_check(var):
    if var == '':
        return True
    else:
        return False


def int_check(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


def positive_check(var):
    if int(var) > 0:
        return True
    else:
        return False


def input_currency_pos(currency_name, currency_lst):
    currency_pos = None
    for i in range(len(currency_lst)):
        if currency_lst[i].lower() == currency_name.lower():
            currency_pos = i
    return currency_pos


def currency_converter(amount, currency, rate):
    currency_result = round(int(amount) * rate)
    output_str = "Конвертированная сумма в " +  currency + " = " + str(currency_result)
    return output_str


currency_list = ["EUR", "USD", "CHF", "GBP", "CNY", "RUB"]
rate_currency_list = [1, 1.1138, 1.0378, 0.8318, 7.0857, 86.6113]

while True:
    print("Выберите валюту из", currency_list)
    target_currency_name = input()
    target_currency_pos = input_currency_pos(target_currency_name, currency_list)
    if target_currency_pos is None:
        print("Введена валюта не из списка. Введите валюту из списка")
        continue
    else:
        target_currency_amount = input("Введите сумму в EUR: ")  
        if empty_check(target_currency_amount):
            print("Вы ввели пустое поле. Введите число.")
        elif not int_check(target_currency_amount):
            print("Вы ввели не число. Введите число.")
        elif not positive_check(target_currency_amount):
            print("Введите положительное число.")
        else:
            converted_amount = currency_converter(target_currency_amount,currency_list[target_currency_pos],rate_currency_list[target_currency_pos])
            print(converted_amount)


    




        






