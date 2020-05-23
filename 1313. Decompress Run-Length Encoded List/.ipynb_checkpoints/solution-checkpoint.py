class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        '''
        input 1D list: 
        [freq,val] pairs
        '''
        #corner case:
        if len(nums)==0:
            #empty
            return None
        #must be even number of elements, thus can take odd/even positions
        #even positions
        val_list = nums[1::2]
        #odd positions
        freq_list = nums[0::2]
        res = []
        for i in range(len(freq_list)):
            res.extend([val_list[i]]*freq_list[i])
        return res