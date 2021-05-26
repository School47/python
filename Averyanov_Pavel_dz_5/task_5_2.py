# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def numberdegenerator(n):

    """возвращает генератор нечетных чисел от одного до n включительно"""

    generator = (num for num in range(1, n+1) if num % 2 == 1)
    return generator


odd_numbers = numberdegenerator(33)
print(type(odd_numbers))
print(*odd_numbers)
