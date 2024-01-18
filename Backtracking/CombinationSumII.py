class Solution(object):
    def combinationSum2(self, candidates, target):
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
        if target < 0:
            return 
        
        if target == 0:
            combination_sums.append(combination_sum[:])
            return 

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            combination_sum.append(candidates[i])
            self.dfs(candidates[i+1:], target-candidates[i], combination_sum, combination_sums)
            combination_sum.pop()
