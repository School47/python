# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.
number = int(input('Введите число от 0 до 20: '))
procentov = [0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
procenta = [2,3,4,]
procent = [1]
if number == 1:
    print(' 1 процент')
elif number in procenta:
    print(number,  " процентa")
elif number in procentov:
    print(number,  " процентов")
else:
    print('Число вне диапазона')


print('====Все склонения для проверки====')
for number in range(0,21,1):
    if number == 1:
        print('1 процент')
    elif number in procenta:
        print(number, "процентa")
    else:
        print(number, "процентов")
