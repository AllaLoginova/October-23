def add_message(function, *args, **kwargs):
    def func(*args, **kwargs):
        print('кто-то вызвал функцию')
        return function(*args, **kwargs)
    return func


@add_message
def add(a, b):
    print(a + b)

@add_message
def sub(a, b):
    print(a - b)


add(1, 5)
sub(6, 2)