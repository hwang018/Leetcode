class Solution:
    def maxScore(self, s: str) -> int:
        s_list = [int(a) for a in list(s)]
        total_ones = sum(s_list)
        #then loop once, track how many ones and zeros encountered
        zero_count = 0
        one_count = 0
        
        res = []
        #must split to 2 non-empty lists
        
        for i,v in enumerate(s_list):
            if v == 0:
                zero_count += 1
            elif v == 1:
                one_count += 1
            res.append((zero_count,total_ones-one_count))
        acc_values = [a[0]+a[1] for a in res]
        
        if acc_values.index(max(acc_values)) == len(acc_values)-1:
            return acc_values[-2]
        else:
            return max(acc_values)