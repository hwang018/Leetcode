class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        import numpy as np
        #when axis = 0, means taking columnar min, axis=1, rowise min
        min_list = list(np.array(matrix).min(axis=1))
        max_list = list(np.array(matrix).max(axis=0))

        return list(set(min_list) & set(max_list)) 