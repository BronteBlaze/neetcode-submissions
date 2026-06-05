class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = []
        postfix = []
        result = []

        l_product = 1
        for i in range(n):
            if i!=0:
                l_product *= nums[i-1]
            prefix.append(l_product)
        
        r_product = 1
        for j in range(n-1, -1, -1):
            if j!=n-1:
                r_product *= nums[j+1]
            postfix.append(r_product)
        
        postfix.reverse()

        for i in range(n):
            result.append(prefix[i]*postfix[i])

        return result