# encoding=utf-8

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i + 1] = key


if __name__ == '__main__':
    a = [5, 2, 4, 6, 1, 3]
    insertion_sort(a)
    print(a)

