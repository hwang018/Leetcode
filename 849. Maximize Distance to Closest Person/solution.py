class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        str_arr = [str(a) for a in seats]
        string_vals = "".join(str_arr)
        new_arr = string_vals.split("1")
        max_val = 0
        max_ind = len(new_arr)-1
        
        for i,v in enumerate(new_arr):
            if v == "":
                continue
            else:
                # group of zeros
                if i in [0,max_ind]:
                    candidate_val = len(v)
                    max_val = int(max(max_val,candidate_val))
                else:
                    # group of zeros in middle segments
                    max_val = int(max(max_val,(len(v)+1)/2))

        return max_val
    
    s
# a better solution using the same concept:

class Solution(object):
    def maxDistToClosest(self, seats):
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)

        return max(ans, seats.index(1), seats[::-1].index(1))