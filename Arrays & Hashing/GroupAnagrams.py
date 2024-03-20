class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_to_string = dict()
        for string in strs:
            anagram = self.get_anagram(string)
            if anagram not in ana_to_string:
                ana_to_string[anagram] = [string]
            else:
                ana_to_string[anagram].append(string)
        res = []
        for anagram in ana_to_string:
            res.append(ana_to_string[anagram])

        
        return res 
    
    def get_anagram(self, string):
        ana = [0] * 26
        for char in string:
            pos = ord(char) - 97
            ana[pos] += 1 
        return str(ana)
