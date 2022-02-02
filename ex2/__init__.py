from ex2 import fetcher
from time import time
CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def timing_decorator(func):
        def wrapper(url):
            # put your code here
            sum_time = 0
            for i in range(num):
                start = time()
                func(url)
                end = time()
                num_time = end - start
                print(num_time)
                sum_time += num_time
            print(sum_time/num)
        return wrapper
    return timing_decorator



@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
