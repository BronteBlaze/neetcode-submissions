class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        max_area = 0

        for i in range(n):
            l_index=i
            r_index=i

            j=i-1
            while j>=0:
                if heights[j]>=heights[i]:
                    l_index=j
                    j-=1
                else:
                    break
            
            k=i+1
            while k<=n-1:
                if heights[k]>=heights[i]:
                    r_index=k
                    k+=1
                else:
                    break
            
            width = r_index-l_index+1
            
            max_area = max(max_area, heights[i]*width)

        return max_area
            
            
