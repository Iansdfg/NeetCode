class Solution:
    def partition(self, s: str) -> List[List[str]]:
        substrings = []
        self.dfs(s, 0, [], substrings)
        return substrings

    def dfs(self, s, index, substring, substrings):
        if index == len(s):
            substrings.append(substring[:])
            return 

        for i in range(index+1, len(s)+1):
            if not self.is_palindrome(s[index:i]):
                continue 
            substring.append(s[index:i])
            self.dfs(s, i, substring, substrings)
            substring.pop()
    
    def is_palindrome(self, s):
        return s == s[::-1]
        
