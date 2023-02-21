from insertion_sort import *
from quick_sort import *
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from tabulate import tabulate
import sys


sys.setrecursionlimit(100000)


def random_list(n):
    a = np.arange(n)
    np.random.shuffle(a)
    return a


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


def test(shuffle=False, nm=10000, i=100, rev=False):
    n = i
    insertion_time = []
    quick_time = []
    incr = []

    while n <= nm:
        incr.append(n)
        if shuffle:
            values = random_list(n)
            insertion_time.append(insertion_test(np.copy(values)))
            quick_time.append(quick_test(np.copy(values)))
        else:
            values = np.arange(n)
            if rev:
                values = values[::-1]
            insertion_time.append(insertion_test(np.copy(values)))
            quick_time.append(quick_test(np.copy(values)))
        print("numero di valori = " + str(n))
        n += i

    table = [["Numero di valori", "Insertion Sort", "Quick Sort"]]
    for i in range(len(incr)):
        tab = [i * 100, insertion_time[i], quick_time[i]]
        table.append(tab)

    if shuffle:
        directory = "rand"
    elif rev:
        directory = "ord_rev"
    else:
        directory = "ord"

    with open(f'data//' + directory + '/sorting_table_n_' + str(nm) + '.txt', 'w') as f:
        f.write(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    plt.figure(1)
    plt.ylabel("Tempo")
    plt.xlabel("Numero di valori")
    plt.plot(incr, insertion_time, label='Insertion Sort')
    plt.plot(incr, quick_time, label='Quick Sort')
    plt.legend()

    plt.savefig(f'img/' + directory + '/' + directory + '_comparison' + str(nm) + '.png')
    plt.clf()


def main():
    test()
    test(rev=True)
    test(True)
    test(True, 1000000, 10000)


if __name__ == "__main__":
    main()
