class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # only 1 condition: longest edge > sum of other 2 edges
        nums.sort()
        # then for each in nums find number of possible edges
        max_ind = len(nums)
        # corner case
        if max_ind < 2:
            return 0
        # starting from index 2
        i = 2
        count = 0
        while i < max_ind:
            l = 0
            r = i-1
            while (l<r):
                if (nums[l]+nums[r]>nums[i]):
                    count += r-l
                    r-=1
                else:
                    l+=1
            i+=1
        return count