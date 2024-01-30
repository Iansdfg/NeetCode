class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        l = 0
        r = 0
        max_len = 0
        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1 
            
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1 
        return max_len
