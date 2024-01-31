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
            if s[r] in char_cnt:
                char_cnt[s[r]] += 1 
            else:
                char_cnt[s[r]] = 1 

            while r - l + 1 - self.get_most_frq(char_cnt) > k:
                char_cnt[s[l]] -= 1 
                l += 1 

            max_len = max(max_len, r - l + 1 )
            r += 1 

        return max_len
    
    def get_most_frq(self, hash_map):
        max_val = 0
        for key in hash_map:
            if hash_map[key] > max_val:
                max_val = hash_map[key]
        return max_val




