# encoding=utf-8

def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    k = p
    while k <= r and i < len(L) - 1 and j < len(R) - 1:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    if k <= r and i == len(L) - 1:
        for x in range(k, r + 1):
            A[k] = R[j]
            j += 1
    elif k <= r and j == len(R) - 1:
        for x in range(k, r + 1):
            A[k] = L[i]
            i += 1


def merge_sort(A, p, r):
    if p < r:
        q = p + (r - p) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


if __name__ == '__main__':
    A = [5, 2, 4, 7, 1, 3, 2, 6]
    merge_sort(A, 0, len(A) - 1)
    print(A)

