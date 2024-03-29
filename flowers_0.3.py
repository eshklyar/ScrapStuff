import itertools as it

class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        count = 0

        # edge case 1 - one element
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                count = 1
        # edge case 2
        else:
            if flowerbed[:2] == [0, 0]:
                count += 1
                flowerbed[0] = 1

            # loop
            for i,num in it.islice(enumerate(flowerbed), 1, len(flowerbed)-1):
                prev = flowerbed[i-1]
                curr = flowerbed[i]
                next = flowerbed[i+1]
                if [prev, curr, next] == [0, 0, 0]:
                    count += 1
                    flowerbed[i] = 1
                    print(count)
            print(count)
            # edge case 3
            print(flowerbed[-3:])
            if flowerbed[-3:] == [1, 0, 0]:
                count += 1
        print(count)
        return count >= n


f = Solution()

# flowerbed = [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
flowerbed = [1,0,0,0,0,1]


n = 2
print(f.canPlaceFlowers(flowerbed, n))



# zero_and_one_list = [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
# print(f"this is zero_and_one_list: {zero_and_one_list}")
#
# prev = 0
# curr = 0
# next = 0
# count = 0
#
# # edge case 1
# if zero_and_one_list[:2] == [0, 0]:
#     count += 1
#     zero_and_one_list[0] = 1
#
# for i,n in it.islice(enumerate(zero_and_one_list), 1, len(zero_and_one_list)-1):
#     # print(f"this is i: {i} and this is n: {n}"
#     prev = zero_and_one_list[i-1]
#     curr = zero_and_one_list[i]
#     next = zero_and_one_list[i+1]
#
#     if [prev, curr, next] == [0, 0, 0]:
#         count += 1
#         zero_and_one_list[i] = 1
#
# # edge case 2
# if zero_and_one_list[-3:] == [1, 0, 0]:
#     count += 1
#
# print(count)