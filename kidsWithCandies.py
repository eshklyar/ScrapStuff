class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        solutionList: [bool] = []
        for i in candies:
            if i + extraCandies >= max(candies):
                solutionList.append(True)
            else:
                solutionList.append(False)
        return solutionList

c= Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(c.kidsWithCandies(candies, extraCandies))