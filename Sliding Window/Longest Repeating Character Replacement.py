class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right =0, 0

        freq = dict()
        res = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while not self.is_valid(freq, right - left +1, k):
                freq[s[left]] -= 1 
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            res = max(res, right - left+1)
        return res

    def is_valid(self, freq, length, k):
        max_f = max(freq.values())
        return length - max_f <= k 

        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 1
        max_len = 1 
        char_cnt = dict()
        char_cnt[s[0]] = 1 

        while right < len(s):
            char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1 
            while not self.is_valid(char_cnt, k):
                if char_cnt[s[left]] > 0:
                    char_cnt[s[left]] -= 1 
                else:
                    del char_cnt[s[left]] 

                left += 1 
      
            max_len = max(max_len, right - left + 1) 
            right += 1 

        return max_len

    def is_valid(self, char_cnt, k):
        length = sum(char_cnt.values())
        max_len = max(char_cnt.values())
        return length - max_len <= k


