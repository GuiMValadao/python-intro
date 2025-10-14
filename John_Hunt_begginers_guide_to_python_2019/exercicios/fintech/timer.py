# Cria um decorador que calcula o tempo para executar um método de classe

from timeit import default_timer
from functools import wraps


def timer(func):
    @wraps(func)
    def inner(self, *variables):
        start = default_timer()
        func(self, *variables)
        end = default_timer()
        print('Retornado de', func.__name__, 'levou', end - start, 'seconds')
        return func
    return inner