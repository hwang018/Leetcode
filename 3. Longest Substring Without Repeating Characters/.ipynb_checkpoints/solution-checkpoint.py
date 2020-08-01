class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        typical dp problem
        ans = either current longest or current val + current longest
        consider the val for longest nonrepeating substring ending at current index
        '''
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        # position of last ecountered char
        last_pos = {s[0]: 0}

        # the length of the longest substring ending at this index
        longest_sub = [1] * len(s)

        for i in range(1, len(s)):
            seen = last_pos.get(s[i], -1) # get value of the key, if not found return -1
            # if the current char is not in current longest substring
            if seen < i - longest_sub[i - 1]:
                # store longest substr length in longest_sub, at each index
                longest_sub[i] = longest_sub[i - 1] + 1
            else:
                longest_sub[i] = i - seen
            # add this element into dict
            last_pos[s[i]] = i

        return max(longest_sub)