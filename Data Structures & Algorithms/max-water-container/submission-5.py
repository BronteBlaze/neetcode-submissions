class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        max_area = 0

        i,j=0,n-1

        while i<j:
            min_height = min(heights[i], heights[j])
            width = j-i
            max_area = max(max_area, min_height*width)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        
        return max_area