import random


class RandomIterator:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return random.randint(1, 100)


rand_iter = RandomIterator()

for i in rand_iter:
    print(i)