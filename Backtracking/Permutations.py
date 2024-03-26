class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutes = []
        visited = set()
        self.dfs(nums, [], permutes, visited)
        return permutes

    def dfs(self, nums, permute, permutes, visited):
        if len(permute) == len(nums):
            permutes.append(permute[:])
            return 

        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            permute.append(nums[i])
            self.dfs(nums, permute, permutes, visited)
            permute.pop()
            visited.remove(nums[i])
