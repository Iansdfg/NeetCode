class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, index, subset, subsets):
        if index > len(nums):
            return 
        subsets.append(subset[:])

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i+1, subset, subsets)
            subset.pop()

        
