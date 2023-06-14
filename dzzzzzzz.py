from datetime import datetime


def time(func):
    def wrapper(val):
        start = datetime.now()
        result = func(val)
        end = datetime.now()
        print('Время работы функции: ', end - start)
        #return result
    return wrapper

@time
def getlist(value):
    new_list = []
    for i in range(value):
        if i % 2 == 0:
            new_list.append(i)
    return new_list

@time
def get_list(value):
    return [x for x in range(value) if x % 2 == 0]


value = 100000000
print(getlist(value), getlist(value))