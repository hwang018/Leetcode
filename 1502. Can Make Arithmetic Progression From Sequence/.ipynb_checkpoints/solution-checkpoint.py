class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        #should sort first
        arr.sort()
        max_ind = len(arr)
        if max_ind==1:
            return True
        i = 1
        curr_set = {arr[1]-arr[0]}
        while i<max_ind:
            diff = arr[i]-arr[i-1]
            if diff not in curr_set:
                return False
            i+=1
        return True