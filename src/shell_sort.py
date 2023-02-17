import math


def shell_sort(a):  # a è l'array
    n = len(a)
    step = math.floor(n / 2)
    while step > 0:
        for i in range(step, n):
            j = i - step
            while j > -1 and a[j] > a[j + step]:
                a[j], a[j + step] = a[j + step], a[j]
                j -= step
        step = math.floor(step / 2)
