class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            count = 0
            for j in words:
                if i in j:
                    count+=1
            
            res.append((i,count))
        
        final_res = [a[0] for a in res if a[1] >= 2]
        return final_res