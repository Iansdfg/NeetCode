class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = r = 0
        char_cnt = dict()
        max_len = 0

        while r < len(s):
            char_cnt[s[r]] = 1 + char_cnt.get(s[r], 0)
            while r - l + 1 - max(char_cnt.values()) > k:
                char_cnt[s[l]] -= 1 
                l += 1 
            max_len = max(max_len, r - l + 1 )
            r += 1 
        return max_len
    
