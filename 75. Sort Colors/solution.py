class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #use 3 pointers, high and low, and current pointer
        p0 = p1 = 0
        p2 = len(nums)-1
        
        while p1<=p2:
            #current value at p1:
            if nums[p1]==0:
                #p0, p1 value exchange, shift 0 to front
                nums[p0],nums[p1] = nums[p1],nums[p0]
                #increment frontier
                p0+=1
                p1+=1
            elif nums[p1]==2:
                #current value is 2, shift to end of arr
                nums[p1],nums[p2] = nums[p2],nums[p1]
                p2-=1
                #don't need to alter p1, it will be tested next loop
            else:
                #current value is 1, only increment current pointer
                p1+=1
                