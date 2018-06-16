#4.1-1
What does FIND-MAXIMUM-SUBARRAY return when all elements of A are negative?

**Solution**
The first two elements as an array.

#4.1-2
Brute-force method of solving maximum-subarray problem.

**Solution**

FIND-MAXIMUM-SUBARRAY(A, low, high):
max-sum = -INF
for i = low to hight
    sum = 0
    for j = i to high
        sum = sum + A[j]
        if sum > max-sum
            max-sum = sum
            max-left = i
            max-right = j
return (max-sum, max-left, max-right)

#4.1-3
See ex_buite_force_max_subarray.py

#4.1-5
TODO
don't understand

