class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        l, r = 0, 0 
        max_len = 0
        cha_set = set()
        while r < len(s):
            while l < r and s[r] in cha_set:
                cha_set.remove(s[l])
                l += 1 
            cha_set.add(s[r])
            r += 1
            
            length = r - l 
            max_len = max(max_len, length)
             
        return max_len

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        l, r = 0, 0 
        max_len = 0
        cha_set = set()
        while r < len(s) :
            if s[r] not in cha_set:
                cha_set.add(s[r])
            else:
                while l < r and s[r] in cha_set:
                    cha_set.remove(s[l])
                    l += 1 
                cha_set.add(s[r])
            r += 1
            
            length = r - l 
            max_len = max(max_len, length)
             
        return max_len

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_cnt = dict()
        left = 0
        res = 0
        for right, char in enumerate(s):
            char_cnt[char] = char_cnt.get(char, 0) + 1

            while not self.is_valid(right - left +1, char_cnt, k):
                char_cnt[s[left]] -= 1 
                if char_cnt[s[left]] == 0:
                    del char_cnt[s[left]]
                left += 1 
            
            res = max(res, right - left+1)
        return res


    def is_valid(self, window_len, char_cnt, k):
        return window_len - max(char_cnt.values()) <= k

        
