class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1 
        max_are = 0
        while l < r:
            water_area = self.count_water(l, r, height)
            max_are = max(max_are, water_area)

            if height[l] >= height[r]:
                r -= 1 
            elif height[l] < height[r]:
                l += 1 
            
        return max_are
            

    def count_water(self, l, r, height):
        water = (r - l) * min(height[l], height[r])
        return water
