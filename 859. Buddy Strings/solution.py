class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        #find all the mismatches between 2 strings 
        A_list = list(A)
        B_list = list(B)
        
        if len(A_list) != len(B_list):
            return False
        if A == "":
            return False
        
        res = []
        
        for i,v in enumerate(A_list):
            if v != B_list[i]:
                #found mismatch:
                res.append((v,B_list[i]))
            else:
                continue
                
        #now res contains all differences
        if len(res) == 0:
            Count_A = Counter(A_list)
            vals = list(Count_A.values())
            if max(vals) >= 2:
                return True
            else:
                return False
        
        else:
            #non-empty res
            if len(res) == 2:
                if (res[1][0],res[0][0]) == (res[0][1],res[1][1]):
                    return True
                else:
                    return False
            else:
                return False