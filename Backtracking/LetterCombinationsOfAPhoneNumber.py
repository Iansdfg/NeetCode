num_char = {
    2:['a', 'b', 'c'],
    3:['d', 'e', 'f'],
    4:['g', 'h', 'i'],
    5:['j', 'k', 'l'],
    6:['m', 'n', 'o'],
    7:['p', 'q', 'r', 's'],
    8:['t', 'u', 'v'],
    9:['w', 'x', 'y', 'z']
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        self.dfs(0, digits, [], res)
        return res


    def dfs(self, level, digits, combination, res):
        if level > len(digits):
            return 
        if len(combination) == len(digits):
            res.append(''.join(combination))
            return 
        chars = num_char[int(digits[level])]

        for i in range(len(chars)):
            combination.append(chars[i])
            self.dfs(level + 1, digits, combination, res)
            combination.pop()
        
