Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Idea:
Sort the list of lists first, this is to reduce the problem to minimum steps.
Such that we can compare ith and i+1 th list.
If the i+1 th list overlaps with ith, we add this merged interval to another storage list.
Each time encountering a new list, we compare with this storage list values and update.
