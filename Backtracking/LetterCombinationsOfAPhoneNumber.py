num_char = {
    '2':['a', 'b', 'c'],
    '3':['d', 'e', 'f'],
    '4':['g', 'h', 'i'],
    '5':['j', 'k', 'l'],
    '6':['m', 'n', 'o'],
    '7':['p', 'q', 'r', 's'],
    '8':['t', 'u', 'v'],
    '9':['w', 'x', 'y', 'z']
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = []
        self.dfs(digits, 0, [], combinations)
        return combinations

    def dfs(self, digits, digit, combination, combinations):
        if digit == len(digits):
            combinations.append(''.join(combination[:]))
            return

        chars = num_char[digits[digit]]
        for char in chars:
            combination.append(char)
            self.dfs(digits, digit + 1, combination, combinations)
            combination.pop()
