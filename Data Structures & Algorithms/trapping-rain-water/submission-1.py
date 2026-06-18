class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        trapped_water = 0

        for i in range(n):
            max_left_height = max(height[0:i+1])
            max_right_height = max(height[i:n])
            trapped_water += min(max_left_height, max_right_height) - height[i]
        
        return trapped_water
