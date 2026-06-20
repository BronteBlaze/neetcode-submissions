class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        trapped_water = 0

        for i in range(n):
            max_left=0
            min_left=0

            max_left = max(height[0:i+1])
            max_right = max(height[i:n])

            minimum = min(max_left, max_right)

            if minimum>height[i]:
                trapped_water += minimum - height[i]
        
        return trapped_water