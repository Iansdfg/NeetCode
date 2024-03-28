class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        combinations = []
        self.dfs(candidates, target, 0, [], combinations)
        return combinations

    def dfs(self, candidates, target, index, combination, combinations):
        if sum(combination) > target:
            return 
        if sum(combination) == target:
            combinations.append(combination[:])
            return 
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue 
            combination.append(candidates[i])
            self.dfs(candidates, target, i + 1, combination, combinations)
            combination.pop()
