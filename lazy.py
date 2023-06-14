import time


class RunningCode:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Время выполнения программы {time.time() - self.start}')

        if exc_type is TypeError:
            return True


with RunningCode() as timer:
    my_list = [x for x in range(1, 100_000_000)]
    my_list += str
    print(timer)