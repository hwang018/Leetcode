Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Idea:
Find columnar max list and rowise min list.
The intersection set is the target. Since all elements are unique in the matrix, when you see one element, it can only be at unique position.