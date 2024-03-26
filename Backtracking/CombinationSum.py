class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.dfs(candidates, 0, target, [], combinations)
        return combinations

    def dfs(self, candidates, index, target, combination, combinations):
        if sum(combination) > target:
            return 
        if sum(combination) == target:
            combinations.append(combination[:])
            return 

        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, i, target, combination, combinations)
            combination.pop()

        
