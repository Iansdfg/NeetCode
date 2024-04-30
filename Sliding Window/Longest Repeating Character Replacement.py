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

        
