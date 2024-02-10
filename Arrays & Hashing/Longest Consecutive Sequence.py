class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for num in nums:
            num_set.add(num)

        max_len = 0
        for num in nums:
            low = num - 1
            if low in num_set:
                continue
            elif low not in num_set:
                high = num + 1
                while high in num_set:
                    high += 1 
            max_len = max(high - num, max_len)
        return max_len

            

        
