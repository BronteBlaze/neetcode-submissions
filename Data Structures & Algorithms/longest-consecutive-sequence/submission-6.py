class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        for i in range(len(nums)):

            j=0
            k=i

            result = [nums[i]]

            while j<len(nums):
                if nums[j]==nums[k]+1:
                    result.append(nums[j])
                    k=j
                    j=0
                else:
                    j+=1
            
            length = max(length, len(result))
        
        return length