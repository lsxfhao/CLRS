#encoding=utf-8

def find_maximum_subarray(A, low, high):
    max_sum = -float("inf")
    max_left = -1
    max_right = -1
    for i in range(low, high):
        sum = 0;
        for j in range(i, high):
            sum += A[j]
            if sum > max_sum:
                max_sum = sum
                max_left = i
                max_right = j
    return (max_left, max_right, max_sum)


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_maximum_subarray(A, 0, 15))
