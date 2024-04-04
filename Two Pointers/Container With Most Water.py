class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = self.area(height, left, right)
        while left < right:
            if height[left] > height[right]:
                right -= 1 
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1 
                right -= 1

            max_area = max(max_area, self.area(height, left, right))

        return max_area


    def area(self, height, left, right):
        h = min(height[left], height[right])
        w = right - left
        return h*w

        
