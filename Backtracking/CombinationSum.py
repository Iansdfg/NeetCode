class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        combination_sums = []
        self.dfs(candidates, target, [], combination_sums)
        return combination_sums
        

    def dfs(self, candidates, target, combination_sum, combination_sums):
        if sum(combination_sum) == target:
            combination_sums.append(combination_sum[:])
            return 
        if sum(combination_sum) > target:
            return 

        for i in range(len(candidates)):
            combination_sum.append(candidates[i])
            self.dfs(candidates[i:], target, combination_sum, combination_sums)
            combination_sum.pop()
