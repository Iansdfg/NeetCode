class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 

        while left + 1 < right:
            mid = (left + right) // 2 

            if nums[mid] == target:
                return mid 

            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else: 
                    left = mid 
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else: 
                    right = mid 
        
        if nums[left] == target:
            return left 
        elif nums[right] == target:
            return right 
        else:
            return -1
