# encoding=utf-8

def find_max_crossing_subarray(A, mid, low, high):
    left_sum = -float('inf')
    max_left = -1
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -float('inf')
    max_right = -1
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(A, low, high):
    if low == high:
        return (low, high, A[low])
    mid = low + (high - low) // 2
    left = find_maximum_subarray(A, low, mid)
    right = find_maximum_subarray(A, mid + 1, high)
    cross = find_max_crossing_subarray(A, mid, low, high)
    if left[2] > right[2] and left[2] > cross[2]:
        return left
    elif left[2] > right[2] and left[2] > cross[2]:
        return right
    else:
        return cross


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_maximum_subarray(A, 0, 15))
