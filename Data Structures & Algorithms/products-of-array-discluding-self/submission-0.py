class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            product = 1

            for j in range(i-1, -1, -1):
                product *= nums[j]
            
            print(product)
            
            for k in range(i+1, n):
                product *= nums[k]
            

            result.append(product)
        
        return result