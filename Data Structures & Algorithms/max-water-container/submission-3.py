class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water = 0

        for i in range(n):
            for j in range(i+1, n):
                width = j-i
                height = min(heights[i], heights[j])
                max_water = max(max_water, width*height)
        
        return max_water