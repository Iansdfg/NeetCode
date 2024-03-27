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
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, index, subset, subsets):
        if index > len(nums):
            return 
        subsets.append(subset[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()
