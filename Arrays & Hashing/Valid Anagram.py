class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_time = dict()
        for char in s:
            char_time[char] = char_time.get(char, 0) + 1 

        for char in t:
            if char not in char_time:
                return False 
            char_time[char] = char_time[char] - 1 
            if char_time[char] == 0:
                del char_time[char]
        return not char_time
