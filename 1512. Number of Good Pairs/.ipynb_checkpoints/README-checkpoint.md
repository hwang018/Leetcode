Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Idea:
Simply use defaultdict, loop each element and store each num's appeared indices as a list.
Then for each of the num (unique), the length of the list will determine how many good pairs
are there. Simply by n choose 2.