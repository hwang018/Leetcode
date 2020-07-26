class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if any 2 overlaps, merge those lists
        # first sort the list of lists, doing sorting as we want to scale down problem
        # to be i and i+1 comparison
        intervals.sort(key=lambda x: x[0])
        # group lists by overlapping, then take the min,max
        merged = []
        for v in intervals:
            if not merged or merged[-1][1] < v[0]:
                merged.append(v)
            else:
                merged[-1][1] = max(merged[-1][1],v[1])
        return merged