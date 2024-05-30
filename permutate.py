class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        sol, ans = [], []
        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans

# s = Solution()

# print(s.permute([1,2,3,4]))


def permute(nums):
    def backtrack(path, used):
        if len(path) == len(nums):
            permutations.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                used[i] = False
                path.pop()

    permutations = []
    backtrack([], [False] * len(nums))
    return permutations

print(permute([1, 2, 3]))



def sol(arr: array, k: int): -> Lis[int]
