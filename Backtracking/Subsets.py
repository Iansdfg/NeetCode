class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        self.dfs(nums, [], subsets)
        return subsets

    def dfs(self, nums, subset, subsets):
        subsets.append(subset[:])

        for i in range(len(nums)):
            subset.append(nums[i])
            self.dfs(nums[i+1:], subset, subsets)
            subset.pop()
