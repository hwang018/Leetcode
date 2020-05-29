class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        #only 2 possible answers for each source-sink pair
        total_sum = sum(distance)
        
        small_index = min(start,destination)
        big_index = max(start,destination)
        
        cost1 = sum(distance[small_index:big_index])
        cost2 = total_sum-cost1
        
        return min(cost1,cost2)
        