class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        indexed_scores = list(enumerate(nums))
        indexed_scores_sorted = sorted(indexed_scores,key=lambda x:x[1],reverse=True)
        
        prepared_ranks = list(range(len(nums)))
        #since it's 1-indexed
        prepared_ranks = [str(a+1) for a in prepared_ranks]
        #alter first 3 elements to text
        prepared_ranks[:3]=["Gold Medal","Silver Medal","Bronze Medal"]

        max_ind = len(indexed_scores_sorted)-1
        d = {}
        
        for i,v in enumerate(indexed_scores_sorted):
            score = v[1]
            #since scores are unique by guarantee, use dict
            rank = prepared_ranks[i]
            d[str(score)] = rank
        print(d)
        
        res = []
        for i in nums:
            res.append(d[str(i)])
        return res