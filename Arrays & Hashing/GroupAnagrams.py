class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagram_strs = dict()
        for string in strs:
            anagram = self.get_anagram(string)
            if anagram in anagram_strs:
                anagram_strs[anagram].append(string)
            else:
                anagram_strs[anagram] = [string]
        res = []
        for anagram in anagram_strs:
            res.append(anagram_strs[anagram])
        return res

    def get_anagram(self, string):
        res = [0]*26
        for char in string:
            res[ord(char)-97] += 1 
        return str(res)




