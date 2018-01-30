# 2.3-1
Using Figure 2.4 as a model, illustrate the operation of merge sort on the array
A = <3, 41, 52, 26, 38, 57, 9, 49>.

**Solution:**
<table>
<tr>
  <td colspan="8">[3, 9, 26, 38, 41, 49, 52, 57]</td>
</tr>
<tr>
  <td colspan="4">[3, 26, 41, 52]</td>
  <td colspan="4">[9, 38, 49, 57]</td>
</tr>
<tr>
  <td colspan="2">[3, 41]</td>
  <td colspan="2">[26, 52]</td>
  <td colspan="2">[38, 57]</td>
  <td colspan="2">[9, 49]</td>
</tr>
<tr>
  <td>3</td> <td>41</td> <td>52</td> <td>26</td> <td>38</td> <td>57</td> <td>9</td> <td>49</td>
</tr>
</table>

# 2.3-2
See rewrite_merge_sort.py

# 2.3-3
//TODO

# 2.3-4
pseudocode:

RECURSIVE-INSERTION-SORT(A, n):
    if n > 1
        RECURSIVE-INSERTION-SORT(A, n - 1)
        INSERT(A, n)

# 2.3-5
Referring back to the searching problem (see Exercise 2.1-3), observe that if the
sequence A is sorted, we can check the midpoint of the sequence against v and
eliminate half of the sequence from further consideration. The binary search algorithm repeats this procedure, halving the size of the remaining portion of the
sequence each time. Write pseudocode, either iterative or recursive, for binary
search. Argue that the worst-case running time of binary search is Θ(lgn).

**Solution**:

iterative search:
```
    BINARY-SEARCH(A, v):
        p = 1
        q = A.length
        r = p + (q - p) / 2
        while A[r] != v and p < q:
            if A[r] > v:
                q = r - 1
                r = p + (q - p) / 2
            else if A[r] < v:
                p = r + 1
                r = p + (q - p) / 2
        if A[r] == v:
            return r
        else
            return null
```

recursive search:
```
    BINARY-SEARCH(A, p, q, v):
        if p < q:
            r = (p + q) / 2
            if A[r] > v:
                return BINARY-SEARCH(A, p, r-1, v)
            else if A[r] < v:
                return BINARY-SEARCH(A, r+1, q, v)
            else:
                return r
        else if p == q and A[p] == v:
            return p
        return null
```

Implementation Code See `binary_search.py`

# 2.3-6
Observe that the while loop of lines 5–7 of the INSERTION-SORT procedure in
Section 2.1 uses a linear search to scan (backward) through the sorted subarray
A[1..j-1]. Can we use a binary search (see Exercise 2.3-5) instead to improve
the overall worst-case running time of insertion sort to Θ(nlgn)?

**Solution**:

No. Although the comparison procedure can be improved, it still need to move all the greater elements to its proper position. This is still Θ(n).

# 2.3-7
//TODO
