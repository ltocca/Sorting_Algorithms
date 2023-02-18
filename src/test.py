from shell_sort import *
from insertion_sort import *
from quick_sort import *
import numpy as np
import random
import time
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from tabulate import tabulate
import sys

sys.setrecursionlimit(100000)


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
    quick_sort(array)
    end = timer()
    return round(end - start, 4)


def test(shuffle=False):
    n = 100
    n_max = 10000
    shell_time = []
    insertion_time = []
    quick_time = []
    incr = []

    while n <= n_max:
        incr.append(n)
        if shuffle:
            shell_time.append(shell_test(random_list(n)))
            insertion_time.append(shell_test(random_list(n)))
            quick_time.append(shell_test(random_list(n)))
        else:
            values = np.arange(n)
            shell_time.append(shell_test(values))
            insertion_time.append(insertion_test(values))
            quick_time.append(quick_test(values))
        n += 100

    table = []
    table.append(["Numero di valori", "Shell Sort", "Insertion Sort", "Quick Sort"])
    for i in range(len(incr)):
        tab = []
        tab.append(i)
        tab.append(shell_time[i])
        tab.append(insertion_time[i])
        tab.append(quick_time[i])
        table.append(tab)

    with open('data/sorting_table.txt', 'w') as f:
        f.write(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    plt.figure(1)
    plt.ylabel("time")
    plt.xlabel("values")
    plt.plot(incr, shell_time, 'g-', label='Shell Sort')
    plt.plot(incr, insertion_time, 'b-', label='Insertion Sort')
    plt.plot(incr, quick_time, 'y-', label='Quick Sort')
    plt.legend()
    plt.savefig(f'img/{"rand" if shuffle else "ord"}/{"_comparison"}.png')
    plt.clf()


def main():
    test()
    test(True)


if __name__ == "__main__":
    main()
