class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        #sort the places of houses and heaters then to find the largest value as gap
        houses.sort()
        heaters.sort()

        j = 0
        out = []
        for house in houses:
            #loop each house, and assign house to heaters
            while j < len(heaters) and house > heaters[j]:
                j+=1

            #then test the min_distance between house and heaters[j] or house and heaters[j-1]
            min_distance = abs(house-heaters[j-1])
            if j < len(heaters):
                #not the end of heaters:
                min_distance = min(min_distance,abs(house-heaters[j]))

            out.append(min_distance)

        return max(out)