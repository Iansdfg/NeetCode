import copy

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        char_cnt = dict()
        for char in s1:
            char_cnt[char] = char_cnt.get(char, 0) + 1

        
        window = s2[:len(s1)]
        window_char_cnt = dict()
        for char in window:
            window_char_cnt[char] = window_char_cnt.get(char, 0) + 1

        r = len(s1)-1
        l = 0
        while r < len(s2):
            if self.is_dict_eq(window_char_cnt, char_cnt):
                return True 

            r += 1 
            if r >= len(s2):
                break
            window_char_cnt[s2[r]] = window_char_cnt.get(s2[r], 0) + 1

            window_char_cnt[s2[l]] = window_char_cnt.get(s2[l], 0) - 1
            if window_char_cnt[s2[l]] <= 0:
                window_char_cnt.pop(s2[l])
            l += 1 

        return False 

    def is_dict_eq(self, dict1, dict2):
        if len(dict1.keys()) != len(dict2.keys()):
            return False 
        for key in dict1.keys():
            if key not in dict2.keys():
                return False
            if dict1[key] != dict2[key]:
                return False 
        return True 
            
                

        
