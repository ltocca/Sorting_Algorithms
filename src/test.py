from shell_sort import *
from insertion_sort import *
from quick_sort import *
import numpy as np
import random
import time
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def random_list(n):
    a = np.arange(n)
    np.random.shuffle(a)
    return a


def shell_test(array):
    start = timer()
    shell_sort(array)
    end = timer()
    return round(end - start, 4)


def insertion_test(array):
    start = timer()
    insertion_sort(array)
    end = timer()
    return round(end - start, 4)


def quick_test(array):
    start = timer()
    shell_sort(array)
    end = timer()
    return round(end - start, 4)


def test(shuffle = False):
    n = 100
    n_max = 10000
    shell_time = []
    insertion_time = []
    quick_time = []
    incr = []

    for i in range(n_max):
        incr.append(n)
        values = np.arange(n)
        if shuffle:
            np.shuffle(values)

        shell_test(values)
        insertion_test(values)
        quick_test(values)
        n += 100

    table = []


def main():
    test()


if __name__ == "__main__":
    main()
