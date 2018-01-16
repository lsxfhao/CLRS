# encoding=utf-8

def selection_sort(a):
    for i in range(0, len(a) - 1):
        key = a[i]
        index = i
        for j in range(i + 1, len(a)):
            if a[j] < key:
                key = a[j]
                index = j
        if a[i] > key:
            a[index] = a[i]
            a[i] = key


if __name__ == '__main__':
    a = [5,3,1,1,6,0,8,9,2,3]
    selection_sort(a)
    print(a)
