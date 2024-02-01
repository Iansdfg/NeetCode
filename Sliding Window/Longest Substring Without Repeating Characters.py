class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = r = 0
        max_len = 0
        char_set = set()
        while r < len(s):
            while l < r and s[r] in char_set:
                char_set.remove(s[l])
                l += 1 

            if s[r] not in char_set:
                char_set.add(s[r])

            max_len = max(max_len, r-l+1)
            r += 1 
        return max_len
