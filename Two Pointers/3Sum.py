class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            two_sums = self.two_sum(nums, 0 - nums[i], i + 1, len(nums))
            for two_sum in two_sums:
                valid = [nums[i]] + two_sum
                valid.sort()
                if valid not in res:
                    res.append(valid)
        return res

    def two_sum(self, nums, target, l, r):
        res = []
        val_pos = dict()
        for i in range(l, r):
            val = nums[i]
            if target - val in val_pos:
                if i != val_pos[target - val]:
                    res.append([target - val, val]) 
        
            val_pos[val] = i 

        return res
