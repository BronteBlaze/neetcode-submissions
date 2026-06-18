class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        trapped_water = 0

        for i in range(n):
            j,k=i-1,i+1

            max_left_height = height[i]
            max_right_height = height[i]

            while j>=0:
                max_left_height = max(max_left_height, height[j])
                j-=1

            print("Max left", max_left_height)

            while k<=n-1:
                max_right_height = max(max_right_height, height[k])
                k+=1

            print("Max right", max_right_height)

            trapped_water += min(max_left_height, max_right_height) - height[i]
        
        return trapped_water

