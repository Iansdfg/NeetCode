class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        subs = []
        self.dfs(s, [], subs)
        return subs


    def dfs(self, s, sub, subs):
        if len(s) == 0:
            subs.append(sub[:])
            return 

        for i in range(1, len(s)+1): # len(s)+1: we need to check if s[:len(s)+1] is_palindrome
            prefix = s[:i]
            print(i, prefix)
            if not self.is_palindrome(prefix):
                continue 

            sub.append(prefix)
            self.dfs(s[i:], sub, subs)
            sub.pop()

    def is_palindrome(self, s):
        return s == s[::-1]

        
