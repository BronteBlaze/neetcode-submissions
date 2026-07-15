class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                min_height = min(heights[i], heights[j])
                width = j-i
                area = min_height * width
                max_area = max(area, max_area)
        
        return max_area