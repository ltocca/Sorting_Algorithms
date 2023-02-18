import random


def quick_sort(a):  # array -> a
    quick_sort_r(a, 1, len(a) - 1)


def quick_sort_r(a, p, r):  # parte ricorsiva del codice, p-> inizio, r->fine
    if p < r:
        q = partition(a, p, r)
        quick_sort_r(a, p, q - 1)
        quick_sort_r(a, q+1, r)


def partition(a, p, r):
    pivot = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


def randomized_quicksort(a, p, r):
    if p < r:
        q = randomized_partition(a, p, r)
        randomized_quicksort(a, p, q - 1)
        randomized_quicksort(a, q + 1, r)


def randomized_partition(a, p, r):
    i = random.choice([p, r])
    a[r], a[i] = a[i], a[r]
    return partition(a, p, r)

