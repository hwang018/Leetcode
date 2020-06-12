class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter
        t_count = Counter(target)
        arr_count = Counter(arr)
        if t_count == arr_count:
            return True
        else:
            return False