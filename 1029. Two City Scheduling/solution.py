class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #consider the difference of each person's 2 options, the bigger the difference, the higher priority
        #that he should fly to cheaper city
        diff = [[(a[1]-a[0]) for a in costs]]
        diff_indexed = list(enumerate(diff[0]))
        diff_indexed_sorted = sorted(diff_indexed, key = lambda x: x[1])
        #first half go city B, second half A
        N = int(len(costs)/2)        
        B_ind = [a[0] for a in diff_indexed_sorted][:N]
        A_ind = [a[0] for a in diff_indexed_sorted][N:]
        total_cost = 0
        
        for i in A_ind:
            #they go A, take [0] cost
            total_cost += costs[i][0]
        for j in B_ind:
            #they go B, take [1] cost
            total_cost += costs[j][1]
            
        return total_cost