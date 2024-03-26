class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutes = []
        visited = [0] * len(nums)
        self.dfs(nums, [], permutes, visited)
        return permutes

    def dfs(self, nums, permute, permutes, visited):
        if len(permute) == len(nums):
            print(permute, visited)
            permutes.append(permute[:])
            return 

        for i in range(len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                continue

            visited[i] = 1
            permute.append(nums[i])
            self.dfs(nums, permute, permutes, visited)
            permute.pop()
            visited[i] = 0
   
