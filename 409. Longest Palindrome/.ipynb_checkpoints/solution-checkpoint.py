class Solution:
    def longestPalindrome(self, s: str) -> int:
        #to be a palindrome, the materials are: if even, dividable by 2 in frequencies 
        #if odd, can add one extra element
        from collections import Counter
        s_count = Counter(list(s))
        #then each unique element, take the biggest frequency that is dividable by 2
        res = 0
        has_extra = 0
        for item in s_count.items():
            val = item[1]
            if val%2 == 0:
                #freq dividable by 2, take all
                res+=val
            elif val == 1:
                has_extra = 1
            else:
                #val = 1:
                res+=(val-1)
                if (val-1)>=1:
                    #assign 1 to flag
                    has_extra = 1
        return res+has_extra