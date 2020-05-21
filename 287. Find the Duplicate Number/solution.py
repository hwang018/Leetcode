class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #assume only 1 duplicated value in list
        #Cycle Detection, use f(x) = nums[x]
        #sequence of x, can form a cycle at duplicated elements occurrence
        #then the problem is to find the entrance of cycle
        #Floyd's algorithm: 2 pointers called tortoise and hare
        #phase 1: hare is twice fast as toitoise, enters cycle and run around the cycle
        #at some point, hare will catch toitoise at intersection
        #but intersection is not the cycle entrance
        
        #tortoise found the length of loop in the first loop and the equation stopping criteria in the second loop makes sure that the two pointers find the beginning and the end (or more like the beginning of a second cycle) of the loop since their distance is the             #length of the loop.
        
        #phase 1 starts, 2 pointers start from 0
        tortoise = hare = nums[0]
        #hare is twice fast as tortoise
        while True:
            #by doing following 2 layers call, we achieve 2 times faster
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                #end of phase 1
                break
        #phase 2
        #send tortoise to origin, a second chance
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare