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

        
