class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[i]*nums[i+1] for i in range(len(nums)-1)) if len(nums) >1 else 0


# nums = [2,3,-2,4]
# nums = [-2,0,-1]
nums = [-2]
s = Solution()
print(s.maxProduct(nums))