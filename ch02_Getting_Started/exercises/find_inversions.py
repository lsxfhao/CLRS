# encoding=utf-8

def merge(A, p, q, r):
    inversions = 0
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            if L[i] != float('inf'):
                inversions += len(L) - i - 1
    return inversions


def find_inversions(A, p, r):
    inversions = 0
    if p < r:
        q = p + (r - p) // 2
        inversions += find_inversions(A, p, q)
        inversions += find_inversions(A, q + 1, r)
        inversions += merge(A, p, q, r)
    return inversions
    

if __name__ == '__main__':
    A = [6, 5, 4, 3, 2, 1]
    inversions = find_inversions(A, 0, len(A) - 1)
    print(inversions)
    print(A)
