class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            total = 0
            for element in nestedList:
                if element.isInteger():
                    total += (element.getInteger() * depth)
                else:
                    total += dfs(element.getList(), depth + 1)

            return total
    
        return dfs(nestedList, 1)