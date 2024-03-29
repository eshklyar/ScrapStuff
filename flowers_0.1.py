class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        prev = 0
        curr = 0
        next = 0
        count = 0
        print(f"this is flowerbed: {flowerbed[flowerbed[len(flowerbed) -1]]}")
        for i,num in enumerate(flowerbed):
            print(f"this is i: {i}")
            print(f"this is num: {num}")
            print(f"this is flowerbed: {flowerbed}")
        if num == 0:
            count += 1
            flowerbed[i] = 1
            print(f"this is flowerbed: {flowerbed}")
#       /*edge case*/
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
#       /*edge case*/
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1
            flowerbed[0] = 1
        for i in range(1, len(flowerbed)-1):
            prev = flowerbed[i-1]
            curr = flowerbed[i]
            next = flowerbed[i+1]
            if prev == 0 and curr == 0 and next == 0:
                count += 1
                flowerbed[i] = 1
        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            print(f"this is flowerbed: {flowerbed}")
            count += 1
            flowerbed[len(flowerbed)-1] = 1

        if count >= n:
            return True
        else:
            return False

f = Solution()
flowerbed = [0,1,2,3,4,5,6,7,8,9]

# flowerbed = [1,0,0,0,1,0,0]
# flowerbed = [1,2,3,4,5,6,7,8,9,10]

n = 2
print(f.canPlaceFlowers(flowerbed, n))



# Compare this snippet from kidsWithCandies.py:
# class Solution:
#     def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
#         solutionList: [bool] = []
#         for i in candies:
#             if i + extraCandies >= max(candies):
#                 solutionList.append(True)
#             else:
#                 solutionList.append(False)
#         return solutionList
#
# c= Solution()
# candies = [2,3,5,1,3]
# extraCandies = 3
# print(c.kidsWithCandies(candies, extraCandies))

