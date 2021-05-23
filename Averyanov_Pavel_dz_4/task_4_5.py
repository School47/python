import utils
import sys

terminal_parameters = sys.argv[1:]
if len(terminal_parameters) > 0: #есть параметры из консоли - используем их
    for element in terminal_parameters:
        result_usd = utils.currency_rates(element)
        print(f"Курс {element} на дату {result_usd[0]} равен {result_usd[1]} рублей")
else:    # запуск из консоли без параметров, либо это не терминал
    result_usd = utils.currency_rates('usd')
    print(f"Курс USD на дату {result_usd[0]} равен {result_usd[1]} рублей")
    result_usd = utils.currency_rates('EUR')
    print(f"Курс EUR на дату {result_usd[0]} равен {result_usd[1]} рублей")