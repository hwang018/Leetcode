class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # consider multiply by 0, store all 0 positions
        zero_positions = []
        non_zero_product = 1
        for i,n in enumerate(nums):
            if n == 0:
                zero_positions.append(i)
            else:
                non_zero_product*=n
        if len(zero_positions) >= 2:
            #always zero result
            return [0]*len(nums)
        elif len(zero_positions) == 1:
            #only 1 zero in list
            res = [0]*len(nums)
            copy = nums[:]
            del copy[zero_positions[0]]
            res[zero_positions[0]] = reduce(lambda x, y: x*y, copy)
            return [int(a) for a in res]
        else:
            #there are no zero
            for i,n in enumerate(nums):
                res.append(non_zero_product/n)
            return [int(a) for a in res]