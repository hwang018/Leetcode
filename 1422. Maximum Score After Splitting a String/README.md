Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Idea:
We first get total number of ones. Then loop once, track accumulated count of zeros and ones.
At each index, create tuple: (zeros,total_ones-ones)
Then the maximum score is the sum of 2 elements tuple. 
Note that we must split into 2 non-empty substrings, therefore we at least should split the second last index. 