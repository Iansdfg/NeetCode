class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left_right = {
            "(" :  ")",
            "{" :  "}",
            "[" :  "]",
        }
        for char in s:
            if char in "([{":
                stack.append(left_right[char])
            else:
                if stack == []:
                    return False 
                top = stack.pop()
                if top !=  char:
                    return False 

        return stack == []
                
