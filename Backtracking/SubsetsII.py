class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        subsets = []
        self.dfs(nums, [], subsets)
        return subsets


    def dfs(self, nums, subset, subsets):
        subsets.append(subset[:])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            subset.append(nums[i])
            self.dfs(nums[i+1:], subset, subsets)
            subset.pop()


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        subsets = []
        self.dfs(nums, subset, subsets, 0)
        return subsets

    def dfs(self, nums, subset, subsets, level):
        subsets.append(subset[:])

        for i in range(level, len(nums)):
            if i > level and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, subset, subsets, i+1)
            subset.pop()


        
