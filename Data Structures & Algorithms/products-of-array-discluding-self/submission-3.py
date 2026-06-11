class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix=1
        for i in range(1, len(result)):
            prefix *= nums[i-1]
            result[i] = prefix
       

        n = len(result)
        postfix=1
        for i in range(n-2, -1, -1):
            postfix *= nums[i+1]
            result[i] *= postfix
        
        return result