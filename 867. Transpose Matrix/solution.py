class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(A[0])
        
        res = []
        for j in range(cols):
            res.append([a[j] for a in A])

        return res