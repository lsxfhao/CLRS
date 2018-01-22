# Ex. 2.2-2
Consider sorting n numbers stored in array A by first finding the smallest element
of A and exchanging it with the element in A[1]. Then find the second smallest
element of A, and exchange it with A[2]. Continue in this manner for the first n - 1
elements of A. Write pseudocode for this algorithm, which is known as selection
sort. What loop invariant does this algorithm maintain? Why does it need to run
for only the first n - 1 elements, rather than for all n elements? Give the best-case
and worst-case running times of selection sort in 成-notation.

**Solution:**
Pseudocode
```
for i = 1 to A.length - 1
    key = A[i]
    index = i
    for j = i + 1 to A.length
        if A[j] < key
            key = A[j]
            index = j
    if A[i] > key
        A[index] = A[i]
        A[i] = key

```
See `ex_selection_sort.py`

Every time it chooses the smallest number, so when the first n-1 elements are sorted, it's certain that the last number is bigger than these before it.
Best case: 成(n)
Worst case: 成(n<sup>2</sup>)

# Ex. 2.2-3
Consider linear search again (see Exercise 2.1-3). How many elements of the input sequence need to be checked on the average, assuming that the element being
searched for is equally likely to be any element in the array? How about in the
worst case? What are the average-case and worst-case running times of linear
search in 成-notation? Justify your answers.

Average case: n/2 (some say (n+1)/2 ?). 成(n)
Worst case: n. 成(n)

# Ex. 2.2-4
How can we modify almost any algorithm to have a good best-case running time?

**//TODO**
