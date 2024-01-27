class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 1
        max_len = 0
        while r <= len(s):
            if self.is_repeat(s[l:r]):
                l += 1 
            max_len = max(max_len, r - l)
            r += 1 
        return max_len

    def is_repeat(self, s):
        rep = set()
        for char in s:
            if char in rep:
                return True
            else:
                rep.add(char)
        return False 
