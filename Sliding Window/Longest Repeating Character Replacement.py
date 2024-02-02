class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = r = 0
        max_len = 0
        char_to_cnt = dict()
        while r < len(s):
            char_to_cnt[s[r]]= char_to_cnt.get(s[r], 0) + 1 
            while r-l+1 - max(char_to_cnt.values()) > k:
                char_to_cnt[s[l]] -= 1 
                l += 1 

            max_len = max(max_len, r-l+1)
            r += 1 

        return max_len


