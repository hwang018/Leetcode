class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        '''
        create a list of intervals, loop once check query time contained by it
        '''
        max_ind = len(startTime)-1
        curr_ind = 0
        
        res=0
        while curr_ind <= max_ind:
            if startTime[curr_ind] <= queryTime <= endTime[curr_ind]:
                res+=1
            curr_ind+=1
        return res