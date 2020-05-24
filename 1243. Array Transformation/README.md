Given an initial array arr, every day you produce a new array using the array of the previous day.

On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:

If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
The first and last elements never change.
After some days, the array does not change. Return that final array.

Idea:
Keep a copy of this arr, get an update function, after each update, it's compared with its previous state results.
Until they are the same, update the curr_arr.
Note that when updating the elements, we need to compare arr with another copy which is intact of any alternation.