

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()  # не вызывается сама по себе, только через вызов внешней ф-ции


# inner_function() # ошибка, NameError, имя не определено
test_function() # вызывается внешняя ф-ция, после срабатывает внутренняя
