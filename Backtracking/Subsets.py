class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        self.dfs(nums, 0, subset, subsets)
        return subsets


    def dfs(self, nums, index, subset, subsets):
        subsets.append(subset[:])
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()

        
