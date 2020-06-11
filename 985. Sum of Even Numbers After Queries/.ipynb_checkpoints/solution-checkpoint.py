class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        S = sum([a for a in A if a%2==0])
        ans = []
        
        for val,ind in queries:
            if A[ind]%2 == 0 and val%2==0:
                #even resultant
                S+=val
                A[ind]+=val
            elif A[ind]%2 != 0 and val%2 != 0:
                #even resultant
                S+=A[ind]
                S+=val
                A[ind]+=val
            else:
                #val odd, A[ind] even
                if A[ind] % 2 == 0:
                    S-=A[ind]
                    A[ind]+=val
                
                else:
                    #val even, A[ind] odd
                    A[ind]+=val
                        
            ans.append(S)
                
        return ans