# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, unique=False):
    """Возвращает n шуток, и без повторений, если unique = True"""
    result = []
    if not unique:
        result.append(f'======= не уникальные {n} шутки ========')
        from random import choice
        for joke in range(1, n+1):
            noun = choice(nouns)
            adv = choice(adverbs)
            adj = choice(adjectives)
            # print(f'шутка номер {joke}:{noun} {adv} {adj}')
            result.append(f'шутка номер {joke}:{noun} {adv} {adj}')

    else:
        result.append(f'======= уникальные {n} шутки ========')
        from random import shuffle
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for noun, adv, adj in zip(nouns, adverbs, adjectives):
            if len(result) <= n:
                result.append(f'{noun} {adv} {adj}')
    return result


jokes_number = input('Введите количество шуток: ')
unique_jokes = int(input('Шутки уникальные? 1 - да, 0 - нет: '))
print(*get_jokes(int(jokes_number), bool(unique_jokes)), sep='\n')
