from timeit import default_timer


def timer(func):
    def inner(value):
        print("calling ", func.__name__, "with", value)
        start = default_timer()
        func(value)
        end = default_timer()
        print("returned from ", func.__name__, "it took", int(end - start), "seconds")

    return inner


@timer
def factorial(num):
    global cache
    if num == 0:
        return 1
    elif num in cache:
        return cache[num]
    else:
        factorial_value = 1
        for i in range(1, num + 1):
            factorial_value = factorial_value * i
        cache[num] = factorial_value
        return factorial_value


cache = {}

print(factorial(150000))
print(factorial(80000))
print(factorial(120000))
print(factorial(150000))
print(factorial(120000))
print(factorial(80000))
