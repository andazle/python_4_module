import time


class RunningCodeJudge:
    def __init__(self):
        self.start = None
    
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Время выполнения программы: {time.time() - self.start}')
        
        if exc_type is TypeError:
            return True


with RunningCodeJudge() as timer:
    my_list = [x for x in range(1, 10_000_000)]
    my_list -= 'str'