## 680.ValidPalindrome II
Allowed to remove at most 1 char from a string, test if we can make it a palindrome.

Idea: by naively trying to remove each element and test, lead to time exceed error. 
Need to design 2 pointers comparing first and last element, like layers in onion.
At some point, there might be a mismatch, then we try to remove either of the position and do a palindrome test. 
Note that we only do palindrome test(more costly) when there's a mismatch.
Until the 2 pointers meet (thus have finished looping the array)