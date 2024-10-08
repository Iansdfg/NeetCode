class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1

        while start + 1 < end:
            mid = (start + end)//2 
            if nums[mid] == target:
                return mid 

            if nums[mid] < nums[start]:
                if nums[mid] < target < nums[start]:
                    start = mid 
                else:
                    end = mid
            else:
                if nums[start] <= target < nums[mid]:
                    end = mid 
                else:
                    start = mid


        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

# <= 的目的是包括所有的点， 比如要包括start，end。 rotate的情况下， start总是大于end，所以line11 可以用target小于 start
# 但也要考虑不rotate的时候，要直接和start比较， 所以line16 需要 start小于等于 target， 不能说 end 小于 target
        




                
