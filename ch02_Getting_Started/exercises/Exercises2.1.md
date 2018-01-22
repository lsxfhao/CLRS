# Ex. 2.1-1
Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the
array A=<31, 41, 59, 26, 41, 58>

**Solution:**
1. <31, **41**, 59, 26, 41, 58>
2. <31, 41, **59**, 26, 41, 58>
3. <31, 41, 59, **26**, 41, 58>
    - a. <31, 41, **26**, 59, 41, 58>
    - b. <31, **26**, 41, 59, 41, 58>
    - c. <**26**, 31, 41, 59, 41, 58>
4. <26, 31, 41, 59, **41**, 58>
    - a. <26, 31, 41, **41**, 59, 58>
5. <26, 31, 41, 41, 59, **58**>
    - a. <26, 31, 41, 41, **58**, 59>
6. <26, 31, 41, 41, 58, 59>

# Ex. 2.1-2
Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.

**Solution:**
See `ex_invert_insertion.py`

# Ex. 2.1-3
Consider the **searching problem**:
**Input:** A sequence of n numbers A = <a1, a2, ..., an> and a value v.
**Output:** An index i such that v = A[i] or the special value NIL if v does not appear in A.
Write pseudocode for linear search, which scans through the sequence, looking
for v. Using a loop invariant, prove that your algorithm is correct. Make sure that
your loop invariant fulfills the three necessary properties.

**Solution:**

PSeudocode:

    index = NIL
    for i = 1 to n
        if v == A[i]
            index = i
    return index

# Ex. 2.1-4
Consider the problem of adding two n-bit binary integers, stored in two n-element
arrays A and B. The sum of the two integers should be stored in binary form in 
an (n+1)-element array C . State the problem formally and write pseudocode for
adding the two integers.

**//TODO**

# Ex. 2.2-1
Express the function n<sup>3</sup>/1000 - 100n<sup>2</sup> - 100n + 3 in terms of Θ-notation.

**Solution:**
Θ(n<sup>3</sup>)

