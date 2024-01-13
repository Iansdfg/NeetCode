class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.get_anagram(s) == self.get_anagram(t)
        

    def get_anagram(self, string):
        res = [0]*26
        for char in string:
            res[ord(char)-97] += 1 
        return str(res)
        
