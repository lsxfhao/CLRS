# 2-1 Insertion sort on small arrays in merge sort
Although merge sort runs in Θ(nlgn) worst-case time and insertion sort runs
in Θ( n<sup>2</sup> ) worst-case time, the constant factors in insertion sort can make it faster in practice for small problem sizes on many machines. Thus, it makes sense to
**coarsen** the leaves of the recursion by using insertion sort within merge sort when
subproblems become sufficiently small. Consider a modification to merge sort in
which n=k sublists of length k are sorted using insertion sort and then merged
using the standard merging mechanism, where k is a value to be determined.

**a**. Show that insertion sort can sort the n/k sublists, each of length k, in Θ(nk) worst-case time.

**Solution**:
The time complexity of insertion sort is Θ(n<sup>2</sup>). To sort a length k list, it costs Θ(k<sup>2</sup>) times. We totally sort n/k sublists, so the time cost is n/k * Θ(k<sup>2</sup>), which we can say is Θ(nk).

**b**. Show how to merge the sublists in Θ(nlg(n/k)) worst-case time.

**Solution**:
The original merge time is Θ(nlgn), because the merge layer is lgn. Now we have the n/k sorted sublists, the merge layer becomes lg(n/k) layers. So the total time is Θ(nlg(n/k)).

**c**. //TODO

**d**. //TODO


# 2-2 Correctness of bubblesort
Bubblesort is a popular, but inefficient, sorting algorithm. It works by repeatedly
swapping adjacent elements that are out of order.

**Solutions**:

**a**. We also need to prove the elements in sorted list are from the original list.

**b**. In every loop, A[j] is the smallest element in A[j...].
Initialization: At start, j = A.length, A[j...] has only one element, it holds.
Maintenance: We campare A[j] and A[j-1] and put the smaller item in A[j-1]. This keeps A[j] the smallest item in the next loop.
Termination: When terminates, j = i, in the previous loop, A[i] is made sure smaller than A[i+1], so A[i] is the smallest item in A[i...].

**c**. At the start of every loop, A[...i-1] is a sorted list.
Initialization: When i = 1, A[...i-1] has no item, it is sorted.
Maintenance: The previous loop made sure that A[i-1] &lt; A[i], and A[i-2] &lt; A[i-1]... So A[...i-1] is a sorted list.
Termination: When i = A.length, A[...i-1] is sorted.

**d**. The worst case running time is Θ(n<sup>2</sup>). Bubblesort usually cost more times because it has more swapping operations to do.


# 2-3 Correctness of Horner’s rule

**Solutions**:

**a**. Θ(n)

**b**. 

    y = 0
    for k = 0 to n
        m = 1
        for i = 1 to k
            m = m * x
        y = y + a_k * m

The running time is Θ(n<sup>2</sup>).

**c**. //TODO

**d**. //TODO

# 2-4 Inversions
Let A[1...n] be an array of n distinct numbers. If i < j and A[i] > A[j], then the
pair (i, j) is called an inversion of A.

**a**. List the five inversions of the array <2, 3, 8, 6, 1>

**Solution**: <br/>
(3, 4), (3, 5), (1, 5), (2, 5), (4, 5)

**b**. What array with elements from the set {1, 2, ... , n} has the most inversions?
How many does it have?

**Solution**:
A = [n, n-1, ... 2, 1]
It has n(n-1)/2 inversions.

**c**. //TODO

**d**. See `find_inversions.py`
