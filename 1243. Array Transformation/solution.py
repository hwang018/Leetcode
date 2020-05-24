class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        
        def update(arr):
            fix_len = len(arr)
            compare_arr = arr[:]
            
            for i,v in enumerate(arr):
                if i in [0,fix_len-1]:
                    #head and tail no change
                    continue
                elif compare_arr[i-1]<v and compare_arr[i+1]<v:
                    #peak element
                    arr[i]-=1
                elif compare_arr[i-1]>v and compare_arr[i+1]>v:
                    arr[i]+=1
            return arr
        
        curr_arr = []

        while curr_arr != arr:
            curr_arr = arr[:]
            arr = update(arr)

        return curr_arr