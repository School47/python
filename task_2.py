#список из нечетных кубов от 1 до 1000
listnumbers = [1]
for number in range(3,999,2):
    listnumbers.append(number ** 3)
#print(listnumbers)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
summnumbers = 0
for numberfromlist in listnumbers:
    alldigits = list(str(numberfromlist)) #разбиваем число в список по цифрам
    summdigits = 0
    for everydigit in alldigits: # считаем сумму цифр числа
        summdigits += int(everydigit)
    if summdigits % 7 == 0: # если сумма цифр делится нацело на 7  то добавляем в сумму
        summnumbers += numberfromlist
print(summnumbers) #выводим итоговую сумму

#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
#Решить задачу под пунктом b, не создавая новый список.
summnumbers = 0
for number in range(0,499,1):
    listnumbers[number] += 17
    alldigits = list(str(listnumbers[number]))  # разбиваем число в список по цифрам
    summdigits = 0
    for everydigit in alldigits:  # считаем сумму цифр числа
        summdigits += int(everydigit)
    if summdigits % 7 == 0:  # если сумма цифр делится нацело на 7  то добавляем в сумму
        summnumbers += numberfromlist
print(summnumbers) #выводим итоговую сумму