class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        substrings = []
        self.dfs(s, [], substrings)
        return substrings

    def dfs(self, s, substring, substrings):
        if len(s) == 0:
            substrings.append(substring[:])
            return 
        for i in range(1, len(s)+1):
            prefix = s[:i]
            if not self.is_palindrome(prefix):
                continue

            substring.append(prefix)
            self.dfs(s[i:], substring, substrings)
            substring.pop()

    def is_palindrome(self, s):
        return s == s[::-1]

        
