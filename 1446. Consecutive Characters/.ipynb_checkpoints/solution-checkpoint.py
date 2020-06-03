class Solution:
    def maxPower(self, s: str) -> int:
        #use 2 pointers to track
        power = 0
        i,j=0,1
        s_list = list(s)
        max_ind = len(s_list)-1 
        if len(s_list) == 0:
            return 0
        elif len(s_list) ==1:
            return 1
        else:
            #max_ind>=1
            curr_val = s_list[i]
            curr_count = 1            
            while j <= max_ind:
                if s_list[j]==curr_val:
                    curr_count+=1
                    power = max(power,curr_count)
                    j+=1
                else:
                    #end of curr substring
                    i = j
                    j += 1
                    power = max(power,curr_count)
                    curr_val = s_list[i]
                    curr_count = 1
                    
        return power