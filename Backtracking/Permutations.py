class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = set()
        permutes = []
        self.dfs(nums, [], permutes, visited)
        return permutes
        

    def dfs(self, nums, permute, permutes, visited):
        if len(permute) == len(nums):
            permutes.append(permute[:])
            return 
            
        for i in range(len(nums)):
            if i in visited:
                continue 

            visited.add(i)
            permute.append(nums[i])
            self.dfs(nums, permute, permutes, visited)
            permute.pop()
            visited.remove(i)
        
