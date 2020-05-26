Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Idea:
Use Counter to store frequencies, for each item, if frequency % 2 ==0, take all of this freq.
else: add freq-1 to the count.
consider corner case of frequency = 1.