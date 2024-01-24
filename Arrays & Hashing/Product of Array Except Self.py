class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        for i in range(len(nums)-1):
            num = nums[i]
            res.append(num*res[-1])

        postfix = 1
        for i in range(len(nums)):
            res[len(nums)-1-i] = res[len(nums)-1-i] * postfix
            postfix = postfix * nums[len(nums) - 1 - i]
            
        return res
        
