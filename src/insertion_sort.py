def insertion_sort(a):
    for j in range(1, len(a)):
        key = [j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
