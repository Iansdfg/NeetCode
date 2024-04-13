class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remain_pos = dict()
        for pos, num in enumerate(nums):
            if num in remain_pos:
                return [pos, remain_pos[num]]
            remain_pos[target - num] = pos
        return [0, 0]

