# encoding=utf-8

def iterative_search(A, v):
    p = 0
    q = len(A) - 1
    r = p + (q - p) // 2
    while A[r] != v and p < q:
        if A[r] > v:
            q = r - 1
            r = p + (q - p) // 2
        elif A[r] < v:
            p = r + 1
            r = p + (q - p) // 2
    if A[r] == v:
        return r
    else:
        return None


def recursive_search(A, p, q, v):
    if p < q:
        r = p + (q - p) // 2
        if A[r] > v:
            return recursive_search(A, p, r - 1, v)
        elif A[r] < v:
            return recursive_search(A, r + 1, q, v)
        else:
            return r
    elif p == q and A[p] == v:
        return p
    return None


if __name__ == '__main__':
    A = [3,4,5,6,7,8,9]
    v = 9
    print(iterative_search(A, v))
    print(recursive_search(A, 0, 6, v))
